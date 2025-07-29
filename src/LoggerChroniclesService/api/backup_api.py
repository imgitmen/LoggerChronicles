import logging
from pathlib import PurePath
import aiofiles
from fastapi import APIRouter, status, Form
from injector import inject
from fastapi_injector import Injected

from application.commands.backup_command_handlers import BackupCommandHandlers
from application.commands.backup_commands import BackupCommand

from .backup_models import BackupPostModel

logger = logging.getLogger(
    f"{__name__}",
)
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
@inject
async def post_data(commandHanlders: BackupCommandHandlers = Injected(BackupCommandHandlers), 
                    data: BackupPostModel = Form(media_type="multipart/form-data") 
                    ):    
        
    cmd = BackupCommand()
    cmd.loggerTypeCode = data.loggerTypeCode
    cmd.loggerSerial = data.loggerSerial
    cmd.timestamp = data.timestamp
    cmd.fileContents = data.file.file.read()
    cmd.filename = data.file.filename
    
    await commandHanlders.backup(cmd)
        
        
    