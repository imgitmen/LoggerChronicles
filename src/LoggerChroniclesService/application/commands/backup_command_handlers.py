import logging
from pathlib import PurePath
import aiofiles
from injector import inject

from LoggerChroniclesService.application.commands.backup_commands import BackupCommand
from LoggerChroniclesService.filesystem_helper import FilesystemHelper


@inject
class BackupCommandHandlers:
    def __init__(self, filesystemHelper: FilesystemHelper):
        self.__filesystemHelper = filesystemHelper
        self.__logger = logging.getLogger()
        
    async def backup(self, cmd: BackupCommand) -> str | None: 
        filePath: str | None = None
        
        backupPath = self.__filesystemHelper.GetBackupPath(cmd.loggerTypeCode, cmd.loggerSerial, cmd.timestamp)
        FilesystemHelper.EnsurePath(backupPath)
        filePath = PurePath(backupPath, cmd.filename)
        
        try:
            async with aiofiles.open(filePath, 'wb') as out_file:
                await out_file.write(cmd.fileContents)
        except Exception as ex:
            self.__logger.error(ex, exc_info=1)
            filePath = None
            
        return filePath
        
        


