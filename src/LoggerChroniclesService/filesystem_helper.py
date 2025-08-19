import datetime
import os
from pathlib import Path, PurePath


class PathInfo:
    relativePath: str
    isFile: bool
    # def __init__(self, path):
    #     self.isFile = Path(path).is_file()
    #     self.fullPath = path

class FilesystemHelper():
    _backupDir: str

    def __init__(self, backupDir: str):
        self._backupDir = backupDir
        
    def EnsurePath(path):
        if not os.path.isdir(path):
            os.makedirs(path)
    
    def GetBackupPath(self, loggerTypeCode: str, loggerSerial: str, timestamp: datetime):
        return Path(self._backupDir, loggerTypeCode, loggerSerial, str(timestamp.year), str(timestamp.month), str(timestamp.day))
            
    def ListDirectories(self, path) -> list[str]:
        return os.listdir(Path.joinpath(self._backupDir, path))
    
    def GetContents(self, path = None) -> list[PathInfo]:
        result = []
        if path is None:
            path = ""
            
        fullpath = Path(self._backupDir, path)
        
        if os.path.exists(fullpath) and fullpath.is_dir():
            for p in os.listdir(fullpath):
                pi = PathInfo()
                fullpath = PurePath(fullpath,p)
                relativePath = "/".join(str(fullpath).replace(self._backupDir, "", 1).split(os.path.sep))
                
                pi.relativePath = relativePath
                pi.isFile = Path(fullpath).is_file()
                result.append(pi)
            
        return result
       
        
    
