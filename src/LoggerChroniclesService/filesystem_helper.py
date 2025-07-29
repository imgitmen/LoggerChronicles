import datetime
import os
from pathlib import Path


class FilesystemHelper():
    _backupDir: str

    def __init__(self, backupDir: str):
        self._backupDir = backupDir
        
    def EnsurePath(path):
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def GetBackupPath(self, loggerTypeCode: str, loggerSerial: str, timestamp: datetime):
        return Path(self._backupDir, loggerTypeCode, loggerSerial, str(timestamp.year), str(timestamp.month), str(timestamp.day))
    
    def Backup(self, loggerTypeCode: str, loggerSerial: str, timestamp: datetime, file):
        backupPath = self.GetBackupPath(loggerTypeCode, loggerSerial, timestamp)
        self.EnsurePath(backupPath)
        
        
    
