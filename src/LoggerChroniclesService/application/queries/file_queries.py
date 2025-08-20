import logging
import os
from pathlib import Path
from injector import inject
from filesystem_helper import FilesystemHelper

class FileInfo:
    fullPath: str
    relativePath: str
    name: str

@inject
class FileQueries:
    def __init__(self, filesystemHelper: FilesystemHelper) -> FileInfo | None:
        self.__filesystemHelper = filesystemHelper
        self.__logger = logging.getLogger()    

    async def getFile(self, relativepath) -> str:
        fi = None
        fullPath = self.__filesystemHelper.ConcatenateRelativePath(relativepath)
        
        if Path(fullPath).is_file():
            fi = FileInfo()
            fi.fullPath = fullPath
            fi.relativePath = relativepath
            fi.name = os.path.basename(fullPath)

        return fi