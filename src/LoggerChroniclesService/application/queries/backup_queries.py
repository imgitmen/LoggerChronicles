import logging
import os
from pathlib import PurePath

from injector import inject
from filesystem_helper import FilesystemHelper


class BackupQuery():
    loggerTypeCode: str | None
    loggerSerial: str | None
    year: str | None
    month: str | None
    day: str | None
    filename: str | None
    
class BackupQueryResultItem:
    relativePath: str
    isFile: bool
    name: str
    
    
@inject
class BackupQueries:
    def __init__(self, filesystemHelper: FilesystemHelper):
        self.__filesystemHelper = filesystemHelper
        self.__logger = logging.getLogger()    

    async def list(self, qry: BackupQuery) -> list[BackupQueryResultItem]:
        result = []
        
        fullPath = PurePath(qry.loggerTypeCode.lower(), 
                            qry.loggerSerial.lower(), 
                            qry.year.lower(), 
                            qry.month.lower(), 
                            qry.day.lower(), 
                            qry.filename.lower())
        
        contents = self.__filesystemHelper.GetContents(fullPath)
        
        for c in contents:
            item = BackupQueryResultItem()
            item.fullpath = c.fullPath
            item.isfile = c.isFile
            item.name = os.path.basename(c.fullPath)
            
            result.append(item)
            
        return result
        
    async def list_path(self, path):
        result = []
        
        fullPath = PurePath(str(path))
        
        contents = self.__filesystemHelper.GetContents(fullPath)
        
        for c in contents:
            item = BackupQueryResultItem()
            item.relativePath = c.relativePath
            item.isFile = c.isFile
            item.name = os.path.basename(c.fullPath)
                        
            result.append(item)
            
        return result
        
        
        
        
        
        
