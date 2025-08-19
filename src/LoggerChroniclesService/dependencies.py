from pathlib import Path
from injector import Module, provider, singleton

from application.security.auth_middleware import AuthService
from config.config_service import ConfigService
from filesystem_helper import FilesystemHelper



class Dependencies(Module):
    @singleton
    @provider
    def provide_config(self) -> ConfigService:
        config_base_path = ConfigService.get_config_basepath()
        appconfig_path = Path(config_base_path, 'config.json')
        return ConfigService(configFilePath=str(appconfig_path))
    
    @singleton
    @provider
    def provide_filesystem_helper(self, config_service: ConfigService) -> FilesystemHelper:
        return FilesystemHelper(config_service.config.backupDir)
    
    @singleton
    @provider
    def provide_auth_service(self, config_service: ConfigService) -> AuthService:
        return AuthService(api_key=config_service.config.api.api_key)

