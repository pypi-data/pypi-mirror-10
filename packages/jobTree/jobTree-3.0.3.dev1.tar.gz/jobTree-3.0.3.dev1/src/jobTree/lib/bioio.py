#!/usr/bin/env python

#Copyright (C) 2006-2012 by Benedict Paten (benedictpaten@gmail.com)
#
#Released under the MIT license, see LICENSE.txt

import sys
import os
import logging
import resource
import logging.handlers
import tempfile
import random
import math
import shutil
from argparse import ArgumentParser
from optparse import OptionParser, OptionContainer, OptionGroup
import subprocess
import xml.etree.cElementTree as ET
from xml.dom import minidom  # For making stuff pretty

# TODO: looks like this can be removed

DEFAULT_DISTANCE = 0.001

defaultLogLevel = logging.INFO

# TODO: looks like this can be removed

loggingFormatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)s %(message)s')

logger = logging.getLogger(__name__)
rootLogger = logging.getLogger()

def getLogLevelString():
    return logging.getLevelName(rootLogger.getEffectiveLevel())

__loggingFiles = []
def addLoggingFileHandler(fileName, rotatingLogging=False):
    if fileName in __loggingFiles:
        return
    __loggingFiles.append(fileName)
    if rotatingLogging:
        handler = logging.handlers.RotatingFileHandler(fileName, maxBytes=1000000, backupCount=1)
    else:
        handler = logging.FileHandler(fileName)
    rootLogger.addHandler(handler)
    return handler


def setLogLevel(level):
    level = level.upper()
    if level == "OFF": level = "CRITICAL"
    # Note that getLevelName works in both directions, numeric to textual and textual to numeric
    numericLevel = logging.getLevelName(level)
    assert logging.getLevelName(numericLevel) == level
    rootLogger.setLevel(numericLevel)

def logFile(fileName, printFunction=logger.info):
    """Writes out a formatted version of the given log file
    """
    printFunction("Reporting file: %s" % fileName)
    shortName = fileName.split("/")[-1]
    fileHandle = open(fileName, 'r')
    line = fileHandle.readline()
    while line != '':
        if line[-1] == '\n':
            line = line[:-1]
        printFunction("%s:\t%s" % (shortName, line))
        line = fileHandle.readline()
    fileHandle.close()
    
def logStream(fileHandle, shortName, printFunction=logger.info):
    """Writes out a formatted version of the given log stream.
    """
    printFunction("Reporting file: %s" % shortName)
    line = fileHandle.readline()
    while line != '':
        if line[-1] == '\n':
            line = line[:-1]
        printFunction("%s:\t%s" % (shortName, line))
        line = fileHandle.readline()
    fileHandle.close()

def addLoggingOptions(parser):
    # Wrapper function that allows jobTree to be used with both the optparse and
    # argparse option parsing modules
    if isinstance(parser, OptionContainer):
        group = OptionGroup(parser, "Logging options",
                            "Options that control logging")
        _addLoggingOptions(group.add_option)
        parser.add_option_group(group)
    elif isinstance(parser, ArgumentParser):
        group = parser.add_argument_group("Logging Options",
                                          "Options that control logging")
        _addLoggingOptions(group.add_argument)
    else:
        raise RuntimeError("Unanticipated class passed to "
                           "addLoggingOptions(), %s. Expecting "
                           "Either optparse.OptionParser or "
                           "argparse.ArgumentParser" % parser.__class__)

supportedLogLevels = (logging.CRITICAL, logging.ERROR, logging.WARNING, logging.INFO, logging.DEBUG)

def _addLoggingOptions(addOptionFn):
    """
    Adds logging options
    """
    # BEFORE YOU ADD OR REMOVE OPTIONS TO THIS FUNCTION, KNOW THAT YOU MAY ONLY USE VARIABLES ACCEPTED BY BOTH
    # optparse AND argparse FOR EXAMPLE, YOU MAY NOT USE default=%default OR default=%(default)s
    defaultLogLevelName = logging.getLevelName( defaultLogLevel )
    addOptionFn("--logOff", dest="logCritical", action="store_true", default=False,
                help="Same as --logCritical")
    for level in supportedLogLevels:
        levelName = logging.getLevelName(level)
        levelNameCapitalized = levelName.capitalize()
        addOptionFn("--log" + levelNameCapitalized, dest="log" + levelNameCapitalized,
                    action="store_true", default=False,
                    help="Turn on logging at level %s and above. (default is %s)" % (levelName, defaultLogLevelName))
    addOptionFn("--logLevel", dest="logLevel", default=defaultLogLevelName,
                help=("Log at given level (may be either OFF (or CRITICAL), ERROR, WARN (or WARNING), INFO or DEBUG). "
                      "(default is %s)" % defaultLogLevelName))
    addOptionFn("--logFile", dest="logFile", help="File to log in")
    addOptionFn("--rotatingLogging", dest="logRotating", action="store_true", default=False,
                help="Turn on rotating logging, which prevents log files getting too big.")

def setLoggingFromOptions(options):
    """
    Sets the logging from a dictionary of name/value options.
    """
    logging.basicConfig()
    rootLogger.setLevel(defaultLogLevel)
    if options.logLevel is not None:
        setLogLevel(options.logLevel)
    for level in supportedLogLevels:
        levelName = logging.getLevelName(level)
        levelNameCapitalized = levelName.capitalize()
        if getattr( options, 'log' + levelNameCapitalized ):
            setLogLevel( levelName )
    logger.info("Logging set at level: %s" % getLogLevelString())
    if options.logFile is not None:
        addLoggingFileHandler(options.logFile, options.logRotating)
        logger.info("Logging to file: %s" % options.logFile)


def system(command):
    logger.debug("Running the command: %s" % command)
    sts = subprocess.call(command, shell=True, bufsize=-1, stdout=sys.stdout, stderr=sys.stderr)
    if sts != 0:
        raise subprocess.CalledProcessError(sts, command)
    return sts

def popen(command, tempFile):
    """Runs a command and captures standard out in the given temp file.
    """
    fileHandle = open(tempFile, 'w')
    logger.debug("Running the command: %s" % command)
    sts = subprocess.call(command, shell=True, stdout=fileHandle, stderr=sys.stderr, bufsize=-1)
    fileHandle.close()
    if sts != 0:
        raise RuntimeError("Command: %s exited with non-zero status %i" % (command, sts))
    return sts

def popenCatch(command, stdinString=None):
    """Runs a command and return standard out.
    """
    logger.debug("Running the command: %s" % command)
    if stdinString != None:
        process = subprocess.Popen(command, shell=True,
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=sys.stderr, bufsize=-1)
        output, nothing = process.communicate(stdinString)
    else:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=sys.stderr, bufsize=-1)
        output, nothing = process.communicate() #process.stdout.read().strip()
    sts = process.wait()
    if sts != 0:
        raise RuntimeError("Command: %s with stdin string '%s' exited with non-zero status %i" % (command, stdinString, sts))
    return output #process.stdout.read().strip()

def popenPush(command, stdinString=None):
    if stdinString == None:
        system(command)
    else:
        process = subprocess.Popen(command, shell=True,
                                   stdin=subprocess.PIPE, stderr=sys.stderr, bufsize=-1)
        process.communicate(stdinString)
        sts = process.wait()
        if sts != 0:
            raise RuntimeError("Command: %s with stdin string '%s' exited with non-zero status %i" % (command, stdinString, sts))

def getTotalCpuTimeAndMemoryUsage():
    """Gives the total cpu time and memory usage of itself and its children.
    """
    me = resource.getrusage(resource.RUSAGE_SELF)
    childs = resource.getrusage(resource.RUSAGE_CHILDREN)
    totalCpuTime = me.ru_utime+me.ru_stime+childs.ru_utime+childs.ru_stime
    totalMemoryUsage = me.ru_maxrss+ me.ru_maxrss
    return totalCpuTime, totalMemoryUsage

def getTotalCpuTime():
    """Gives the total cpu time, including the children.
    """
    return getTotalCpuTimeAndMemoryUsage()[0]

def getTotalMemoryUsage():
    """Gets the amount of memory used by the process and its children.
    """
    return getTotalCpuTimeAndMemoryUsage()[1]

def absSymPath(path):
    """like os.path.abspath except it doesn't dereference symlinks
    """
    curr_path = os.getcwd()
    return os.path.normpath(os.path.join(curr_path, path))

#########################################################
#########################################################
#########################################################
#testing settings
#########################################################
#########################################################
#########################################################

class TestStatus:
    ###Global variables used by testing framework to run tests.
    TEST_SHORT = 0
    TEST_MEDIUM = 1
    TEST_LONG = 2
    TEST_VERY_LONG = 3

    TEST_STATUS = TEST_SHORT

    SAVE_ERROR_LOCATION = None

    def getTestStatus():
        return TestStatus.TEST_STATUS
    getTestStatus = staticmethod(getTestStatus)

    def setTestStatus(status):
        assert status in (TestStatus.TEST_SHORT, TestStatus.TEST_MEDIUM, TestStatus.TEST_LONG, TestStatus.TEST_VERY_LONG)
        TestStatus.TEST_STATUS = status
    setTestStatus = staticmethod(setTestStatus)

    def getSaveErrorLocation():
        """Location to in which to write inputs which created test error.
        """
        return TestStatus.SAVE_ERROR_LOCATION
    getSaveErrorLocation = staticmethod(getSaveErrorLocation)

    def setSaveErrorLocation(dir):
        """Set location in which to write inputs which created test error.
        """
        logger.info("Location to save error files in: %s" % dir)
        assert os.path.isdir(dir)
        TestStatus.SAVE_ERROR_LOCATION = dir
    setSaveErrorLocation = staticmethod(setSaveErrorLocation)

    def getTestSetup(shortTestNo=1, mediumTestNo=5, longTestNo=100, veryLongTestNo=0):
        if TestStatus.TEST_STATUS == TestStatus.TEST_SHORT:
            return shortTestNo
        elif TestStatus.TEST_STATUS == TestStatus.TEST_MEDIUM:
            return mediumTestNo
        elif TestStatus.TEST_STATUS == TestStatus.TEST_LONG:
            return longTestNo
        else: #Used for long example tests
            return veryLongTestNo
    getTestSetup = staticmethod(getTestSetup)

    def getPathToDataSets():
        """This method is used to store the location of
        the path where all the data sets used by tests for analysis are kept.
        These are not kept in the distrbution itself for reasons of size.
        """
        assert "SON_TRACE_DATASETS" in os.environ
        return os.environ["SON_TRACE_DATASETS"]
    getPathToDataSets = staticmethod(getPathToDataSets)

def saveInputs(savedInputsDir, listOfFilesAndDirsToSave):
    """Copies the list of files to a directory created in the save inputs dir,
    and returns the name of this directory.
    """
    logger.info("Saving the inputs: %s to the directory: %s" % (" ".join(listOfFilesAndDirsToSave), savedInputsDir))
    assert os.path.isdir(savedInputsDir)
    #savedInputsDir = getTempDirectory(saveInputsDir)
    createdFiles = []
    for fileName in listOfFilesAndDirsToSave:
        if os.path.isfile(fileName):
            copiedFileName = os.path.join(savedInputsDir, os.path.split(fileName)[-1])
            system("cp %s %s" % (fileName, copiedFileName))
        else:
            copiedFileName = os.path.join(savedInputsDir, os.path.split(fileName)[-1]) + ".tar"
            system("tar -cf %s %s" % (copiedFileName, fileName))
        createdFiles.append(copiedFileName)
    return createdFiles

def getBasicOptionParser(usage="usage: %prog [options]", version="%prog 0.1", parser=None):
    if parser is None:
        parser = OptionParser(usage=usage, version=version)

    addLoggingOptions(parser)

    parser.add_option("--tempDirRoot", dest="tempDirRoot", type="string",
                      help="Path to where temporary directory containing all temp files are created, by default uses the current working directory as the base.",
                      default=os.getcwd())

    return parser

def parseBasicOptions(parser):
    """Setups the standard things from things added by getBasicOptionParser.
    """
    (options, args) = parser.parse_args()

    setLoggingFromOptions(options)

    #Set up the temp dir root
    if options.tempDirRoot == "None":
        options.tempDirRoot = os.getcwd()

    return options, args

def parseSuiteTestOptions(parser=None):
    if parser is None:
        parser = getBasicOptionParser()

    parser.add_option("--testLength", dest="testLength", type="string",
                     help="Control the length of the tests either SHORT/MEDIUM/LONG/VERY_LONG. default=%default",
                     default="SHORT")

    parser.add_option("--saveError", dest="saveError", type="string",
                     help="Directory in which to store the inputs of failed tests")

    options, args = parseBasicOptions(parser)
    logger.info("Parsed arguments")

    if options.testLength == "SHORT":
        TestStatus.setTestStatus(TestStatus.TEST_SHORT)
    elif options.testLength == "MEDIUM":
        TestStatus.setTestStatus(TestStatus.TEST_MEDIUM)
    elif options.testLength == "LONG":
        TestStatus.setTestStatus(TestStatus.TEST_LONG)
    elif options.testLength == "VERY_LONG":
        TestStatus.setTestStatus(TestStatus.TEST_VERY_LONG)
    else:
        parser.error('Unrecognised option for --testLength, %s. Options are SHORT, MEDIUM, LONG, VERY_LONG.' %
                     options.testLength)

    if options.saveError is not None:
        TestStatus.setSaveErrorLocation(options.saveError)

    return options, args

def nameValue(name, value, valueType=str, quotes=False):
    """Little function to make it easier to make name value strings for commands.
    """
    if valueType == bool:
        if value:
            return "--%s" % name
        return ""
    if value is None:
        return ""
    if quotes:
        return "--%s '%s'" % (name, valueType(value))
    return "--%s %s" % (name, valueType(value))

def getRandomAlphaNumericString(length=10):
    """Returns a random alpha numeric string of the given length.
    """
    return "".join([ random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for i in xrange(0, length) ])

def makeSubDir(dirName):
    """Makes a given subdirectory if it doesn't already exist, making sure it us public.
    """
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        os.chmod(dirName, 0777)
    return dirName

def getTempFile(suffix="", rootDir=None):
    """Returns a string representing a temporary file, that must be manually deleted
    """
    if rootDir is None:
        handle, tmpFile = tempfile.mkstemp(suffix)
        os.close(handle)
        return tmpFile
    else:
        tmpFile = os.path.join(rootDir, "tmp_" + getRandomAlphaNumericString() + suffix)
        open(tmpFile, 'w').close()
        os.chmod(tmpFile, 0777) #Ensure everyone has access to the file.
        return tmpFile

def getTempDirectory(rootDir=None):
    """
    returns a temporary directory that must be manually deleted. rootDir will be
    created if it does not exist.
    """
    if rootDir is None:
        return tempfile.mkdtemp()
    else:
        if not os.path.exists(rootDir):
            try:
                os.makedirs(rootDir)
            except OSError:
                # Maybe it got created between the test and the makedirs call?
                pass
            
        while True:
            # Keep trying names until we find one that doesn't exist. If one
            # does exist, don't nest inside it, because someone else may be
            # using it for something.
            tmpDir = os.path.join(rootDir, "tmp_" + getRandomAlphaNumericString())
            if not os.path.exists(tmpDir):
                break
                
        os.mkdir(tmpDir)
        os.chmod(tmpDir, 0777) #Ensure everyone has access to the file.
        return tmpDir

class TempFileTree:
    """A hierarchical tree structure for storing directories of files/dirs/

    The total number of legal files is equal to filesPerDir**levels.
    filesPerDer and levels must both be greater than zero.
    The rootDir may or may not yet exist (and may or may not be empty), though
    if files exist in the dirs of levels 0 ... level-1 then they must be dirs,
    which will be indexed the by tempfile tree.
    """
    def __init__(self, rootDir, filesPerDir=500, levels=3):
        #Do basic checks of input
        assert(filesPerDir) >= 1
        assert(levels) >= 1
        if not os.path.isdir(rootDir):
            #Make the root dir
            os.mkdir(rootDir)
            open(os.path.join(rootDir, "lock"), 'w').close() #Add the lock file

        #Basic attributes of system at start up.
        self.levelNo = levels
        self.filesPerDir = filesPerDir
        self.rootDir = rootDir
        #Dynamic variables
        self.tempDir = rootDir
        self.level = 0
        self.filesInDir = 1
        #These two variables will only refer to the existance of this class instance.
        self.tempFilesCreated = 0
        self.tempFilesDestroyed = 0

        currentFiles = self.listFiles()
        logger.info("We have setup the temp file tree, it contains %s files currently, \
        %s of the possible total" % \
        (len(currentFiles), len(currentFiles)/math.pow(filesPerDir, levels)))

    def getTempFile(self, suffix="", makeDir=False):
        while 1:
            #Basic checks for start of loop
            assert self.level >= 0
            assert self.level < self.levelNo
            assert os.path.isdir(self.tempDir)
            #If tempDir contains max file number then:
            if self.filesInDir > self.filesPerDir:
                #if level number is already 0 raise an exception
                if self.level == 0:
                    raise RuntimeError("We ran out of space to make temp files")
                #Remove the lock file
                os.remove(os.path.join(self.tempDir, "lock"))
                #reduce level number by one, chop off top of tempDir.
                self.level -= 1
                self.tempDir = os.path.split(self.tempDir)[0]
                self.filesInDir = len(os.listdir(self.tempDir))
            else:
                if self.level == self.levelNo-1:
                    self.filesInDir += 1
                    #make temporary file in dir and return it.
                    if makeDir:
                        return getTempDirectory(rootDir=self.tempDir)
                    else:
                        return getTempFile(suffix=suffix, rootDir=self.tempDir)
                else:
                    #mk new dir, and add to tempDir path, inc the level buy one.
                    self.tempDir = getTempDirectory(rootDir=self.tempDir)
                    open(os.path.join(self.tempDir, "lock"), 'w').close() #Add the lock file
                    self.level += 1
                    self.filesInDir = 1

    def getTempDirectory(self):
        return self.getTempFile(makeDir=True)

    def __destroyFile(self, tempFile):
        #If not part of the current tempDir, from which files are being created.
        baseDir = os.path.split(tempFile)[0]
        if baseDir != self.tempDir:
            while True: #Now remove any parent dirs that are empty.
                try:
                    os.rmdir(baseDir)
                except OSError:
                    break
                baseDir = os.path.split(baseDir)[0]
                if baseDir == self.rootDir:
                    break

    def destroyTempFile(self, tempFile):
        """Removes the temporary file in the temp file dir, checking its in the temp file tree.
        """
        #Do basic assertions for goodness of the function
        assert os.path.isfile(tempFile)
        assert os.path.commonprefix((self.rootDir, tempFile)) == self.rootDir #Checks file is part of tree
        #Update stats.
        self.tempFilesDestroyed += 1
        #Do the actual removal
        os.remove(tempFile)
        self.__destroyFile(tempFile)

    def destroyTempDir(self, tempDir):
        """Removes a temporary directory in the temp file dir, checking its in the temp file tree.
        The dir will be removed regardless of if it is empty.
        """
        #Do basic assertions for goodness of the function
        assert os.path.isdir(tempDir)
        assert os.path.commonprefix((self.rootDir, tempDir)) == self.rootDir #Checks file is part of tree
        #Update stats.
        self.tempFilesDestroyed += 1
        #Do the actual removal
        try:
            os.rmdir(tempDir)
        except OSError:
            shutil.rmtree(tempDir)
            #system("rm -rf %s" % tempDir)
        self.__destroyFile(tempDir)

    def listFiles(self):
        """Gets all files in the temp file tree (which may be dirs).
        """
        def fn(dirName, level, files):
            if level == self.levelNo-1:
                for fileName in os.listdir(dirName):
                    if fileName != "lock":
                        absFileName = os.path.join(dirName, fileName)
                        files.append(absFileName)
            else:
                for subDir in os.listdir(dirName):
                    if subDir != "lock":
                        absDirName = os.path.join(dirName, subDir)
                        assert os.path.isdir(absDirName)
                        fn(absDirName, level+1, files)
        files = []
        fn(self.rootDir, 0, files)
        return files

    def destroyTempFiles(self):
        """Destroys all temp temp file hierarchy, getting rid of all files.
        """
        os.system("rm -rf %s" % self.rootDir)
        logger.debug("Temp files created: %s, temp files actively destroyed: %s" % (self.tempFilesCreated, self.tempFilesDestroyed))

#########################################################
#########################################################
#########################################################
#misc input/output functions
#########################################################
#########################################################
#########################################################

def getNextNonCommentLine(file):
    line = file.readline()
    while line != '' and line[0] == '#':
        line = file.readline()
    return line

def removeNewLine(line):
    if line != '' and line[-1] == '\n':
        return line[:-1]
    return line

def readFirstLine(inputFile):
    i = open(inputFile, 'r')
    j = removeNewLine(i.readline())
    i.close()
    return j

def padWord(word, length=25):
    if len(word) > length:
        return word[:length]
    if len(word) < length:
        return word + " "*(length-len(word))
    return word
    
#########################################################
#########################################################
#########################################################
#Generic file functions
#########################################################
#########################################################
#########################################################

def catFiles(filesToCat, catFile):
    """Cats a bunch of files into one file. Ensures a no more than maxCat files
    are concatenated at each step.
    """
    if len(filesToCat) == 0: #We must handle this case or the cat call will hang waiting for input
        open(catFile, 'w').close()
        return
    maxCat = 25
    system("cat %s > %s" % (" ".join(filesToCat[:maxCat]), catFile))
    filesToCat = filesToCat[maxCat:]
    while len(filesToCat) > 0:
        system("cat %s >> %s" % (" ".join(filesToCat[:maxCat]), catFile))
        filesToCat = filesToCat[maxCat:]

def prettyXml(elem):
    """ Return a pretty-printed XML string for the ElementTree Element.
    """
    roughString = ET.tostring(elem, "utf-8")
    reparsed = minidom.parseString(roughString)
    return reparsed.toprettyxml(indent="  ")

def isNewer(firstFile, secondFile):
    """Returns True if the first file was modified more recently than the second file (used os.path.getctime)
    """
    assert os.path.exists(firstFile)
    assert os.path.exists(secondFile)
    return os.path.getctime(firstFile) > os.path.getctime(secondFile)

def main():
    pass

def _test():
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    _test()
    main()
