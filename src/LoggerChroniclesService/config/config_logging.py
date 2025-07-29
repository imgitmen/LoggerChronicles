import seqlog
import logging
from pathlib import Path

import yaml

from LoggerChroniclesService.config.config_service import ConfigService


def configure_logging():
    __configfilepath = Path(ConfigService.get_config_basepath(), "logging.yml")
    
    logging.info("will try to configure logging from file %s", __configfilepath)
    
    if Path(__configfilepath).is_file():
        #logging.config.fileConfig(__configfilepath)
        try:
            seqlog.configure_from_file(__configfilepath)
        except Exception as ex:
            print(ex)
            config = None
            with open(__configfilepath, "r") as f:
                config = yaml.safe_load(f)
                
            logging.config.dictConfig(config)
    else:
        logging.info("file %s does not exists", __configfilepath)