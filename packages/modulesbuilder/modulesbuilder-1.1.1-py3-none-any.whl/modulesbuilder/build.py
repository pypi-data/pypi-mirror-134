#!/usr/bin/env python3

import yaml
import sys
import os
import shutil
import docker
import json
import re

from .module import unameFields, INDENT
from .modules import *

from colorama import Fore, Back, Style

class ModuleExistsError(FileExistsError):
    pass

class ModulefileExistsError(FileExistsError):
    pass

force = False
modulesPrefix = '/usr/local/Modules'

def print_red(s):
    print(Fore.RED + s + Fore.WHITE)

def print_yellow(s):
    print(Fore.YELLOW+ s + Fore.WHITE)

DEBUG = 0

def modulefileHeader(module):
    header = "#%Module\n##\n"
    header += "## " + module.id() + "\n"
    header += "##\n"
    header += "set sysname    [uname sysname]\n"
    header += "set machine    [uname machine]\n"
    header += "set domain     [uname domain]\n"
    header += "set os_release [uname release]\n"
    header += "set os_version [uname version]\n"
    header += "set nodename   [uname nodename]\n"
    return header + "\n"

def modulefileHelp(module, indent):
    helpStr = indent + "proc ModulesHelp { } {\n"
    lines = module.help().split("\n")
    for i in range(0, len(lines)-1):
        line = lines[i].replace('"', '\\"')
        helpStr += indent + INDENT + "puts stderr \"" + line + "\"\n"

    # Footer
    helpStr += indent + INDENT + "puts stderr \"\"\n"
    helpStr += indent + INDENT + "puts stderr \"" + INDENT + "version: " + module.version() + "\"\n"
    if module.website():
        helpStr += indent + INDENT + "puts stderr \"" + INDENT + "website: " + module.website() + "\"\n"
    helpStr += indent + "}\n"
    return helpStr

def modulefileConflicts(module, indent):
    # always conflict with other versions of the same modules
    conflicts = module.conflicts()
    conflictStr = ""
    for c in conflicts:
        conflictStr += indent + "conflict " + c + "\n"
    return conflictStr

def modulefileDepends(module, indent):
    dependStr = ""
    for d in module.depends():
        dependStr += indent + "module load %s; prereq %s\n" % (d, d)
    return dependStr

def modulefileDependsNoUnload(module, indent):
    dependStr = ""
    for d in module.dependsSticky():
        dependStr += indent + "if {![is-loaded %s]} { module load %s }; prereq %s\n" % (d, d, d)
    return dependStr

# Set the prefix to the root of the module software
def modulefilePrefix(module, indent, prefix):
    if module.prefix():
        return indent + "set prefix %s/\n" %(module.prefix())
    else:
        return indent + "set prefix %s/sw/%s/%s\n" %(prefix, module.name(), module.version())

def modulefileBody(module, indent, prefix):
    body = ""
    body += modulefileHelp(module, indent)
    body += modulefileConflicts(module, indent)
    body += modulefileDepends(module, indent)
    body += modulefileDependsNoUnload(module, indent)
    body += modulefilePrefix(module, indent, prefix)
    # Set the interior body from configuration
    if module.body:
        lines = module.body().split("\n")
        for i in range(0, len(lines)-1):
            body += indent + lines[i] + "\n"
    return body

def constructBody(modules, unameValues, unameFields, i, depth, prevModID, string, prefix):
    # string for every indentation
    indent = INDENT

    # stop condition, out of unameValues fields
    if (i >= len(unameFields)):
        return string

    field = unameFields[i];
    if DEBUG: print(depth*indent + "key: " + field)

    # TODO: doesn't work when no uname fields defined
    if (len(unameValues[field]) > 0):
        # Start switch block for unameValues field
        string += depth*indent + "switch -glob $" + field + " {\n"
        depth += 1

        # add all field values
        for value in unameValues[field]:
            # module's identified by their vield values
            thisModID = prevModID + value

            # check if there are any modules along this field path, or skip.
            # this prevents us from printing out blocks for fields that
            # no module is using
            path = 0
            for moduleID in modules.keys():
                if (thisModID == moduleID[0:len(thisModID)]):
                    path = 1
                    break;
            if (path == 0):
                continue

            # Start case block for unameValues field value
            string += depth*indent + value + " {\n"
            if DEBUG: print(depth*indent + "prevModID: " + thisModID)

            # Add matching module or descend to the next unameValues field
            if thisModID in modules:
                string += modulefileBody(modules[thisModID], (depth+1)*indent, prefix)
            else:
                if DEBUG: print(depth*indent + "descending to next unameValues field")
                string = constructBody(modules, unameValues, unameFields, i+1, depth+1, thisModID, string, prefix)

            # End case block for unameValues field value
            string += (depth)*indent + "}\n"

        # End switch block for unameValues field
        string += (depth-1)*indent + "}\n"
    else:
        # No unameValues field values, try the next unameValues field
        string = constructBody(modules, unameValues, unameFields, i+1, depth, prevModID, string, prefix)

    return string


def createModulefile(modules, moduleDir, prefix, force=False, verbose=False):
    try:
        rootModule = modules[0]
    except:
        print("Found no valid modules")
        sys.exit(1)

    # collect all the uname values
    unameValues = dict()
    for module in modules:
        for field in unameFields:
            if field in module.yml:
                if not field in unameValues:
                    unameValues[field] = []
                unameValues[field] = list(set(unameValues[field] + [module.yml[field]]))

    # set the active fields, adding default value for modules that don't
    # specify a value
    activeFields = []
    for field in unameFields:
        if field in unameValues:
            unameValues[field] += ["default"]
            activeFields.append(field)

    # Associate modules with their uname field values
    moduleID = dict()
    for module in modules:
        modID = ""
        for field in activeFields:
            if field in module.yml:
                modID += module.yml[field]
            else:
                modID += "default"
        moduleID[modID] = module
        #DEBUG
        if DEBUG: print(modID)
        #print (module)

    body = constructBody(moduleID, unameValues, activeFields, 0, 0, "", "", prefix)

    # Determine path to modulefile
    modulefileDir = moduleDir + "/modulefiles"
    modulefileDir += "/" + rootModule.name()
    modulefile = modulefileDir + "/" + rootModule.version()
    if DEBUG: print(modulefile)

    try:
        os.makedirs(modulefileDir)
    except FileExistsError:
        pass # do nothing
    if (~force & os.path.exists(modulefile)):
        raise ModulefileExistsError("Modulefile '%s' exists, set force=True to overwrite" % modulefile)
    f = open(modulefile, "w+")
    f.write(modulefileHeader(modules[0]))
    f.write(body)
    f.close()

def createVersionFile(modules, moduleDir, force=False, verbose=False):
    defaults = dict()
    for module in modules:
        if module.defaultVersion():
            if not module.name() in defaults:
                defaults[module.name()] = module.defaultVersion()
            else:
                print("WARNING: multiple defaults for %s set in config" % module.name())
    for name in defaults.keys():
        modulefileDir = "%s/%s" % (moduleDir, name)
        try:
            os.makedirs(modulefileDir)
        except FileExistsError:
            pass # do nothing
        versionFile = "%s/.version" % (modulefileDir)
        versionStr = "#%%Module##\nmodule-version %s default\n" %(defaults[name])
        if (~force & os.path.exists(versionFile)):
            raise ModulefileExistsError("Version file '%s' exists, set force=True to overwrite" % versionFile)
        if (verbose):
            print("Creating version file %s" % versionFile)
        f = open(versionFile, "w+")
        f.write(versionStr)
        f.close()

def writeDockerLogs(logs, logFile):
    with open(logFile, 'w') as out:
        for log in logs:
            try:
                out.write((log['stream']))
            except:
                pass


def dockerWriteLog(data, f):
    line = dockerLogString(data)
    f.write(line)
    return line

def dockerLogString(data):
    try:
        return json.loads(data,encoding="utf-8")['stream']
    except:
        return json.dumps(json.loads(data,encoding="utf-8"))

def build(module, modulePath, buildPath, modulesPrefix, target, verbose=False, force=False):
    client = docker.from_env()
    cli = docker.APIClient()

    path = modulePath
    tag = ("module_%s-%s-%s" % (module.name(), module.version(), target.replace(":","-"))).lower()
    dockerfile = "%s/%s" % (path, module.dockerfile())
    user = "%d:%d" % (os.getuid(), os.getgid())
    logFile = "%s/log/%s.log" %(buildPath, tag)
    moduleBuildPath = "%s/sw/%s/%s" % (buildPath, module.name(), module.version())
    moduleInstallPath = "%s/sw/%s/%s" % (modulesPrefix, module.name(), module.version())

    logs = []
    buildargs = dict()
    buildargs['MODULES_PREFIX'] = modulesPrefix
    buildargs['MODULE_PATH'] = moduleInstallPath
    buildargs['MODULE_NAME'] = module.name()
    buildargs['MODULE_VERS'] = module.version()
    buildargs['TARGET'] = target

    # open log file
    try: os.makedirs("%s/log" % buildPath)
    except FileExistsError: pass
    f = open(logFile, 'w')

    if (os.path.exists(moduleBuildPath)):
        if (force):
            shutil.rmtree(moduleBuildPath)
        else:
            raise ModuleExistsError("Module '%s' exists, set force=True to overwrite" % moduleBuildPath)

    if verbose: print("  creating docker image %s" %(tag))
    response = [dockerWriteLog(line, f) for line in cli.build(path=path, tag=tag, dockerfile=dockerfile, buildargs=buildargs, rm=True)]

    # TODO not catching build errors
    regex = re.compile('^Successfully built.*')
    lastLine = response[-2] #TODO this is a bit cludgy
    #print(response)
    if regex.match(lastLine) == None:
        print_red("  docker image build failed for module %s/%s: %s" %(
            module.name(), module.version(), lastLine))
        return False

    try:
        image = client.images.get(tag)
        if verbose: print("  running docker image %s" %(tag))
        try: os.makedirs(buildPath)
        except FileExistsError: pass
        try: os.makedirs(moduleBuildPath)
        except FileExistsError: pass
        host_config = client.api.create_host_config(binds={
            buildPath: { 'bind': modulesPrefix, 'mode': 'ro', },
            moduleBuildPath: { 'bind': moduleInstallPath, 'mode': 'rw', } })
        container = cli.create_container(tag, user=user, volumes=[modulesPrefix, moduleBuildPath], host_config=host_config)
        containerID = container.get("Id")
        cli.start(containerID)
        logs = cli.logs(containerID, follow=True, stream=True)
        for log in logs:
            f.write(log.decode("utf-8"))
        ret = cli.wait(containerID)
        cli.remove_container(containerID)
        if (ret.get('StatusCode') != 0):
            print_red("  build failed for module %s/%s, see log file %s" %(module.name(), module.version(), logFile))
            return False
    except docker.errors.ImageNotFound as error:
        if (os.path.exists(moduleBuildPath)): os.remove(moduleBuildPath)
        shutil.rmtree(moduleBuildPath)
        print_red("  docker image build failed for module %s/%s: %s" %(module.name(), module.version(), error))
        return False

    return True

def buildModulefile(modules, path = "modules", prefix = "/usr/local/Modules", verbose = False, force = False, debug = False, target = "ubuntu:18.04") :
    createModulefile(modules, path, prefix, force=force)
    createVersionFile(modules, path, force=force)

def buildModule(module, path = "modules", prefix = "/usr/local/Modules", verbose = False, force = False, debug = False, target = "ubuntu:18.04") :
    buildPath = os.path.abspath(path)
    modulePath = os.path.abspath(os.path.dirname(module.config()))
    buildSucceeded = build(module, modulePath, buildPath, prefix, target=target, verbose=verbose, force=force)

def buildFromConfig(config, path = "modules", prefix = "/usr/local/Modules", verbose = False, force = False, debug = False, target = "ubuntu:18.04") :

    modules = getModules(config)

    # Divide the modules up into their respective name/version
    modulesGroups = dict()
    for module in modules:
        group = module.id()
        if not group:
            print("empty group id")
            continue
        if not group in modulesGroups:
            modulesGroups[group] = []
        modulesGroups[group] += [module]

    # Spin off a single modulefile for each group
    for group in modulesGroups.keys():
        for module in modulesGroups[group]:
            buildModule(module, path, prefix, verbose, force, debug, target)
        # only each group needs a modulefile
        buildModulefile(group, path, prefix, verbose, force, debug, target)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("module", help="modulefile config", type=str)
    parser.add_argument("-p", "--prefix", default="/usr/local/Modules",
                        help="modules prefix, the path to mount point")
    parser.add_argument("-o", "--output-dir", default="build",
                        help="build modules in output directory")
    parser.add_argument("-v", "--verbose",
                        help="toggle verbose output",
                        action="store_true")
    parser.add_argument("-f", "--force",
                        help="force rebuild of docker images",
                        action="store_true")
    parser.add_argument("-t", "--target", help="target os", default="ubuntu:16.04")
    args = parser.parse_args()
    yamlFile = args.module
    modulePath = os.path.dirname(os.path.abspath(yamlFile))
    moduleDir = args.output_dir
    modulesPrefix = args.prefix
    verbose = args.verbose
    force = args.force
    target = args.target
    build(config=yamlFile, path=moduleDir, prefix=modulesPrefix, verbose=verbose, debug=DEBUG, force=force, target=target)
