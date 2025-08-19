import logging
import os
from pathlib import Path
from dotenv import load_dotenv
from injector import Injector

from api import start_api
from config.config_logging import configure_logging
from dependencies import Dependencies



if __name__ == "__main__":
    env_file = Path(os.environ['HOME'], ".env")
    load_dotenv(env_file)

    print('LOGGER_CHRONICLES_HOME: '+ os.environ['LOGGER_CHRONICLES_HOME'])
    
    configure_logging()
    
    try:
        logging.info("Starting Logger Chronicle Service")
        dependency_injector = Injector([Dependencies()])
        start_api(dependency_injector)

    except Exception as ex:
        logging.exception("Error occurred starting application")