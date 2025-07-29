from datetime import datetime


class BackupCommand():
    loggerTypeCode: str
    loggerSerial: str
    timestamp: datetime
    fileContents: bytearray
    filename: str
