from fastapi import FastAPI, Depends
from fastapi_injector import attach_injector
import uvicorn

from api import backup_api, file_api
from application.security.auth_middleware import AuthService, authMiddleware
from config.config import Config
from config.config_service import ConfigService



def start_api(dependency_injector):
    api = FastAPI(docs_url="/api/docs", 
        dependencies=[Depends(authMiddleware(dependency_injector.get(AuthService)))])
    
    api.include_router(
        backup_api.router, 
        prefix="/api/v1/backup"
    )
    
    api.include_router(
        file_api.router, 
        prefix="/api/v1/file"
    )
    
    configService = dependency_injector.get(ConfigService)
    config = Config.load_dict(configService.config)
    
    attach_injector(api, dependency_injector)
    
    uvicorn.run(app=api, host=config.api.host, port=config.api.port, log_level="info")
