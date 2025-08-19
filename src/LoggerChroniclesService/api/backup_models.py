from datetime import datetime
from typing import Annotated, Optional
from fastapi import File, Form, UploadFile, Path
from pydantic import BaseModel

class BackupPostModel(BaseModel):
    loggerTypeCode: Annotated[str, Form()]
    loggerSerial: Annotated[str, Form()]
    timestamp: Annotated[datetime, Form()]
    file: Annotated[UploadFile, File()]
    
class BackupQueryModel(BaseModel):
    loggerTypeCode: Annotated[str, Path(min_length=0)]
    loggerSerial: Annotated[str, Path(min_length=0)]
    year: Annotated[str, Path(min_length=0)]
    month: Annotated[str, Path(min_length=0)] 
    day: Annotated[str, Path(min_length=0)]
    filename: Annotated[str, Path(min_length=0)]
    
