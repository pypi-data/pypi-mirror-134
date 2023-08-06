import tempfile
import os
import time
import asyncio
import properties
import pathlib
from pathlib import Path

class log:
    def __init__(self, logName: str):
        """This function is need to create new log instance"""
 
        self.name = logName
        # self.messageTypesSet = messageTypesSet
 
        self._loggingStatus = True
        self._loggingMirrorStatus = False
        self._loggingMirrors = []
        self.logFile = tempfile.TemporaryFile(mode="r+")
 
        self.logFile.write(self._makeLogString("info", "logholm", "Info", f"Log initialized as {self.name} in a {self.logFile.name} tempfile. Logholm {properties.logholmVersionPrefix} v{properties.logholmVersion} ({properties.logholmVersionCodename})."))
 
    def _makeLogString(self, prefix: str, issuer: str, type: str, message: str):
        logLine = f"{time.ctime(time.time())} | {prefix}@{issuer}:{type}~$ {message}\n"
        return logLine
 
    def logMessage(self, prefix: str, type: str, message: str):
        if self._loggingStatus == True:
            logLine = self._makeLogString(prefix, self.name, type, message)
            self.logFile.write(logLine)

            self._sendToLogMirrors(logLine)
 
    def loggingMirrorInit(self, file: str):
        if self._loggingStatus == True:
            self._loggingMirrorStatus = True
            self._loggingMirrors.append(file)
 
            self.logFile.seek(0)
 
            with open(file, "w") as fileToEdit:
                for line in self.logFile.readlines():
                    fileToEdit.write(line)

    def _sendToLogMirrors(self, logLine):
        if self._loggingMirrorStatus == True:
            for file in self._loggingMirrors:
                with open(file, "a") as file:
                    file.write(logLine)

    def logPrint(self):
        self.logFile.seek(0)
        print(self.logFile.read())
 
    def logPrintLineSwap(self):
        self.logFile.seek(0)
        for line in self.logFile.readlines():
            print(line)
 
    def logSaveToFile(self, file: str):
        self.logFile.seek(0)
        with open(file, "w") as fileToEdit:
            for line in self.logFile.readlines():
                fileToEdit.write(line)
 
    def logCommit(self):
        if self._loggingStatus == True:
            line = self._makeLogString("info", "logholm", "Info", f"Log {self.name} is commited. Logholm {properties.logholmVersionPrefix} v{properties.logholmVersion} ({properties.logholmVersionCodename}). Now log is only for read.")
            self.logFile.write(line)
            self._sendToLogMirrors(line)
            self._loggingStatus = False
 
    def logClose(self):
        os.unlink(self.logFile.name)