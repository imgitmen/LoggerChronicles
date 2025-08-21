import logging
import mimetypes
from fastapi import APIRouter, Response, status, Form, Path
from fastapi.responses import FileResponse, StreamingResponse
from injector import inject
from fastapi_injector import Injected

from application.queries.file_queries import FileQueries


router = APIRouter()


@router.get("/{filepath:path}", status_code=status.HTTP_200_OK)
@inject
async def download_file(response: Response, queryHandlers: FileQueries = Injected(FileQueries), filepath: str = ""):
    logging.getLogger(f"{__name__}").debug("GET File endpoint responding with params '{Params}'", Params = filepath)

    fi = await queryHandlers.getFile(filepath)
    
    if fi is not None:
        mimeType = mimetypes.guess_type(fi.fullPath)
        response.headers["Content-Disposition"] = f"attachment; filename={fi.name}"
        response.headers["Content-Type"] = mimeType[0]
        return FileResponse(str(fi.fullPath), filename=fi.name)
    else:
        response.status_code = status.HTTP_404_NOT_FOUND