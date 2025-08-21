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
async def post_file(response: Response, commandHanlders: BackupCommandHandlers = Injected(BackupCommandHandlers), 
                    data: BackupPostModel = Form(media_type="multipart/form-data") 
                    ):    
    print("name:" + __name__)
    logging.getLogger(f"{__name__}").debug("POST Backup endpoint responding with params '{Params}'", Params = data)
    relativePath = None
    
    cmd = BackupCommand()
    cmd.loggerTypeCode = data.loggerTypeCode
    cmd.loggerSerial = data.loggerSerial
    cmd.timestamp = data.timestamp
    cmd.fileContents = data.file.file.read()
    cmd.filename = data.file.filename
    
    relativePath = await commandHanlders.backup(cmd)
    
    if relativePath is not None:
        response.headers["location"] = relativePath
    

@router.get("/", status_code=status.HTTP_200_OK)
@router.get("/{path:path}", status_code=status.HTTP_200_OK)
@inject
async def navigate(response: Response, queryHandlers: BackupQueries = Injected(BackupQueries), path: Optional[str] = ""):
    logging.getLogger(f"{__name__}").debug("GET Backup endpoint responding with params '{Params}'", Params = path)
    
    queryresult = await queryHandlers.list_path(path.strip())
    
    if queryresult is not None:
        return JSONResponse(content=jsonable_encoder(queryresult))
    else:
        response.status_code = status.HTTP_404_NOT_FOUND

