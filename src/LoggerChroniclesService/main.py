import logging
import os
from pathlib import Path
from injector import Injector

from api import start_api
from config.config_logging import configure_logging
from dependencies import Dependencies



if __name__ == "__main__":
    print('LOGGER_CHRONICLES_HOME: '+ os.environ['LOGGER_CHRONICLES_HOME'])
    
    configure_logging()
    
    try:
        logging.info("Starting Logger Chronicle Service")
        dependency_injector = Injector([Dependencies()])
        start_api(dependency_injector)

    except Exception as ex:
        logging.exception("Error occurred starting application")