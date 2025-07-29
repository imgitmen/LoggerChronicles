import os
from pathlib import Path
from typing import Dict
from .config import Config

class ConfigService():
    config: Dict
    def __init__(self, configFilePath: str) -> Config:
        self.config = Config.load_json(configFilePath)
        
    @staticmethod
    def get_config_basepath():
        base_path = Path(os.environ['LOGGER_CHRONICLES_HOME'], "_config")
        return base_path