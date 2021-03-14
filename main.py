import os

from settings import LOGS_PATH
from loguru import logger
from utils.working_with_selenium import SeleniumWorksWithSite


if __name__ == "__main__":
    if not os.path.exists(LOGS_PATH):
        os.mkdir(LOGS_PATH)
    logger.add(
        os.path.join(LOGS_PATH, "file_{time}.log"),
        format="{name} {message}",
        level="INFO",
        rotation="5 MB",
    )
    try:
        driver_selenium = SeleniumWorksWithSite(site_url="https://www.python.org")
    except Exception as excp:
        print(f"Job was finished because of {excp}")
        logger.error(f"Job was finished because of {excp}")
