import logging
from pathlib import PurePath
from typing import Annotated, Optional
import aiofiles
from fastapi import APIRouter, Response, status, Form, Path
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from injector import inject
from fastapi_injector import Injected

from application.queries.backup_queries import BackupQueries, BackupQuery
from api.backup_models import BackupPostModel, BackupQueryModel
from application.commands.backup_command_handlers import BackupCommandHandlers
from application.commands.backup_commands import BackupCommand


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

@router.get("/", status_code=status.HTTP_200_OK)
@router.get("/{path:path}", status_code=status.HTTP_200_OK)
@inject
async def get_data(response: Response, queryHandlers: BackupQueries = Injected(BackupQueries), path: Optional[str] = ""):
    
    queryresult = await queryHandlers.list_path(path.strip())
    
    return JSONResponse(content=jsonable_encoder(queryresult))

@router.get("/file/{filepath:path}", status_code=status.HTTP_200_OK)
@inject
async def download_file(response: Response, queryHandlers: BackupQueries = Injected(BackupQueries), filepath: str = ""):
    pass