import os
import logging
import eons as e
import platform
import shutil
import jsonpickle
from distutils.file_util import copy_file
from distutils.dir_util import copy_tree
from distutils.dir_util import mkpath
from abc import abstractmethod
from subprocess import Popen
from subprocess import PIPE
from subprocess import STDOUT

######## START CONTENT ########
# All builder errors
class BuildError(Exception): pass


# Exception used for miscillaneous build errors.
class OtherBuildError(BuildError): pass


# Project types can be things like "lib" for library, "bin" for binary, etc. Generally, they are any string that evaluates to a different means of building code.
class ProjectTypeNotSupported(BuildError): pass


class EBBS(e.Executor):

    def __init__(self):
        super().__init__(name="eons Basic Build System", descriptionStr="A hackable build system for all languages!")

        self.RegisterDirectory("language")
        self.RegisterDirectory("inc/language")
        self.RegisterDirectory("ebbs/inc/language")

    #Override of eons.Executor method. See that class for details
    def RegisterAllClasses(self):
        super().RegisterAllClasses()
        self.RegisterAllClassesInDirectory(os.path.join(os.path.dirname(os.path.abspath(__file__)), "language"))

    #Override of eons.Executor method. See that class for details
    def AddArgs(self):
        super().AddArgs()
        self.argparser.add_argument('dir', type = str, metavar = '/project/build', help = 'path to build folder', default = '.')
        self.argparser.add_argument('-l','--language', type = str, metavar = 'cpp', help = 'language of files to build', dest = 'lang')

    #Override of eons.Executor method. See that class for details
    def ParseArgs(self):
        super().ParseArgs()

        if (not self.args.lang):
            self.ExitDueToErr("You must specify a language.")

    #Override of eons.Executor method. See that class for details
    def UserFunction(self, **kwargs):
        super().UserFunction(**kwargs)
        self.Build()

    #Run a build script.
    def Execute(self, language, dir, repoData, **kwargs):
        builder = self.GetRegistered(language, "build")
        builder(executor=self, dir=dir, repo=repoData, **kwargs)

    #Build things!
    def Build(self):
        repoData = {}
        if (self.args.repo_store and self.args.repo_url and self.args.repo_username and self.args.repo_password):
            repoData = {
                'store': self.args.repo_store,
                'url': self.args.repo_url,
                'username': self.args.repo_username,
                'password': self.args.repo_password
            }

        self.Execute(self.args.lang, self.args.dir, repoData, **self.extraArgs)



class Builder(e.UserFunctor):
    def __init__(self, name=e.INVALID_NAME()):
        super().__init__(name)

        self.requiredKWArgs.append("dir")

        self.supportedProjectTypes = []

        # TODO: project is looking an awful lot like a Datum.. Would making it one add functionality?
        self.projectType = "bin"
        self.projectName = e.INVALID_NAME()

        self.clearBuildPath = True

    # Build things!
    # Override this or die.
    @abstractmethod
    def Build(self):
        raise NotImplementedError

    # RETURN whether or not the build was successful.
    # Override this to perform whatever success checks are necessary.
    # This will be called before running the next build step.
    def DidBuildSucceed(self):
        return True

    # Sets the build path that should be used by children of *this.
    # Also sets src, inc, lib, and dep paths, if they are present.
    def PopulatePaths(self, buildPath):
        self.buildPath = buildPath

        # TODO: Consolidate this code with more attribute hacks?
        rootPath = os.path.abspath(os.path.join(self.buildPath, "../"))
        if (os.path.isdir(rootPath)):
            self.rootPath = rootPath
        else:
            self.rootPath = None
        srcPath = os.path.abspath(os.path.join(self.buildPath, "../src"))
        if (os.path.isdir(srcPath)):
            self.srcPath = srcPath
        else:
            self.srcPath = None
        incPath = os.path.abspath(os.path.join(self.buildPath, "../inc"))
        if (os.path.isdir(incPath)):
            self.incPath = incPath
        else:
            self.incPath = None
        depPath = os.path.abspath(os.path.join(self.buildPath, "../dep"))
        if (os.path.isdir(depPath)):
            self.depPath = depPath
        else:
            self.depPath = None
        libPath = os.path.abspath(os.path.join(self.buildPath, "../lib"))
        if (os.path.isdir(libPath)):
            self.libPath = libPath
        else:
            self.libPath = None

    # Projects should have a name of {project-type}_{project-name}.
    # For information on how projects should be labelled see: https://eons.dev/convention/naming/
    # For information on how projects should be organized, see: https://eons.dev/convention/uri-names/
    # RETURNS modified kwargs.
    def PopulateProjectDetails(self, **kwargs):
        self.os = platform.system()
        self.PopulatePaths(kwargs.pop("dir"))
        details = os.path.basename(os.path.abspath(os.path.join(self.buildPath, "../"))).split("_")
        self.projectType = details[0]
        if (len(details) > 1):
            self.projectName = '_'.join(details[1:])
        self.repo = kwargs.pop("repo")
        configPath = os.path.join(self.rootPath, "config.json")
        self.config = None
        if (os.path.isfile(configPath)):
            configFile = open(configPath, "r")
            self.config = jsonpickle.decode(configFile.read())
        return kwargs

    # Hook for any pre-build configuration
    def PreBuild(self, **kwargs):
        pass

    # Hook for any post-build configuration
    def PostBuild(self, **kwargs):
        # TODO: Do we need to clear self.buildPath here?
        pass

    # Creates the folder structure for the next build step.
    # RETURNS the next buildPath.
    def PrepareNext(self, nextBuilder):
        logging.debug(f"Preparing for next builder: {nextBuilder['language']}")
        nextPath = f"{nextBuilder['type']}_{nextBuilder['name']}"
        mkpath(nextPath)
        if ("copy" in nextBuilder):
            for cpy in nextBuilder["copy"]:
                # logging.debug(f"copying: {cpy}")
                for src, dst in cpy.items():
                    destination = os.path.join(nextPath, dst)
                    mkpath(destination)
                    logging.debug(f"Copying {src} to {destination}")
                    if os.path.isfile(src):
                        copy_file(src, destination)
                    elif os.path.isdir(src):
                        copy_tree(src, destination)
        nextConfigFile = os.path.join(nextPath, "config.json")
        logging.debug(f"writing: {nextConfigFile}")
        nextConfig = open(nextConfigFile, "w")
        nextConfig.write(jsonpickle.encode(nextBuilder["config"]))
        nextConfig.close()
        return nextPath

    # Runs the next Builder.
    # Uses the Executor passed to *this.
    def BuildNext(self, **kwargs):
        if (not self.config or "ebbs_next" not in self.config):
            logging.info("Build process complete!")
            return

        for nxt in self.config["ebbs_next"]:
            nxtPath = os.path.join(self.PrepareNext(nxt), nxt["buildPath"])
            logging.debug(f"Executing {nxt['language']} in {nxtPath} with repo {self.repo} and args {kwargs}")
            self.executor.Execute(language=nxt["language"], dir=nxtPath, repoData=self.repo, **kwargs)

    # Override of eons.Functor method. See that class for details
    def UserFunction(self, **kwargs):
        self.executor = kwargs.pop("executor")
        kwargs = self.PopulateProjectDetails(**kwargs)
        self.buildPath = os.path.join(self.rootPath, self.buildPath)
        if(self.clearBuildPath):
            if (os.path.exists(self.buildPath)):
                logging.info(f"DELETING {self.buildPath}")
                shutil.rmtree(self.buildPath)
            mkpath(self.buildPath)
            os.chdir(self.buildPath)
        self.PreBuild(**kwargs)
        if (len(self.supportedProjectTypes) and self.projectType not in self.supportedProjectTypes):
            raise ProjectTypeNotSupported(
                f"{self.projectType} is not supported. Supported project types for {self.name} are {self.supportedProjectTypes}")
        logging.info(f"Using {self.name} to build {self.projectName}, a {self.projectType}")
        self.Build()
        self.PostBuild(**kwargs)
        if (self.DidBuildSucceed()):
            self.BuildNext(**kwargs)
        else:
            logging.error("Build did not succeed.")

    # RETURNS: an opened file object for writing.
    # Creates the path if it does not exist.
    def CreateFile(self, file, mode="w+"):
        mkpath(os.path.dirname(os.path.abspath(file)))
        return open(file, mode)

    # Run whatever.
    # DANGEROUS!!!!!
    # TODO: check return value and raise exceptions?
    # per https://stackoverflow.com/questions/803265/getting-realtime-output-using-subprocess
    def RunCommand(self, command):
        p = Popen(command, stdout=PIPE, stderr=STDOUT, shell=True)
        while True:
            line = p.stdout.readline()
            if (not line):
                break
            print(line.decode('utf8')[:-1])  # [:-1] to strip excessive new lines.

