import logging
from pathlib import PurePath
import aiofiles
from injector import inject

from application.commands.backup_commands import BackupCommand
from filesystem_helper import FilesystemHelper


@inject
class BackupCommandHandlers:
    def __init__(self, filesystemHelper: FilesystemHelper):
        self.__filesystemHelper = filesystemHelper
        self.__logger = logging.getLogger()
        
    async def backup(self, cmd: BackupCommand) -> str | None: 
        relativePath: str | None = None
        
        backupPath = self.__filesystemHelper.GetBackupPath(cmd.loggerTypeCode.lower(), cmd.loggerSerial.lower(), cmd.timestamp)
        FilesystemHelper.EnsurePath(backupPath)
        filePath = PurePath(backupPath, cmd.filename.lower())
        
        try:
            async with aiofiles.open(filePath, 'wb') as out_file:
                await out_file.write(cmd.fileContents)
        except Exception as ex:
            self.__logger.error(ex, exc_info=1)
            raise ex
        
        relativePath = self.__filesystemHelper.MakeRelativePath(filePath)
        
        return relativePath[1:]
        
        


