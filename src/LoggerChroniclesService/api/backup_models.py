from datetime import datetime
from typing import Annotated
from fastapi import File, Form, UploadFile
from pydantic import BaseModel

class BackupPostModel(BaseModel):
    loggerTypeCode: Annotated[str, Form()]
    loggerSerial: Annotated[str, Form()]
    timestamp: datetime
    file: Annotated[UploadFile, File()]
    