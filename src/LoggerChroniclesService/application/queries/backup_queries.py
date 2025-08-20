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

    def __populateItems(self, contents) -> list[BackupQueryResultItem]:
        result = []

        for c in contents:
            item = BackupQueryResultItem()
            item.relativePath = c.relativePath
            item.isfile = c.isFile
            item.name = os.path.basename(c.relativePath)
            
            result.append(item)
            
        return result

    async def list_path(self, path) -> list[BackupQueryResultItem] | None :
        result = None
        
        fullPath = PurePath(str(path))
        
        contents = self.__filesystemHelper.GetContents(fullPath)
        
        if contents is not None:
            result = self.__populateItems(contents)
            
        return result

    async def list(self, qry: BackupQuery) -> list[BackupQueryResultItem] | None :
        result = None
        
        fullPath = PurePath(qry.loggerTypeCode.lower(), 
                            qry.loggerSerial.lower(), 
                            qry.year.lower(), 
                            qry.month.lower(), 
                            qry.day.lower(), 
                            qry.filename.lower())
        
        return await self.list(fullPath)