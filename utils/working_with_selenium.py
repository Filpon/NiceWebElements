import time
import os

from settings import LOGS_PATH
from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class SeleniumWorksWithSite:
    """
	Class for working with Site via Selenium
	"""

    def __init__(self, site_url):
        logger.add(
            os.path.join(LOGS_PATH, "web_elements_{time}.log"),
            level="INFO",
            rotation="10 MB",
        )
        self.chrome_options = Options()
        # self.chrome_options.headless = True  # uncomment for visible chrome mode
        self.driver = webdriver.Chrome(
            executable_path="./drivers/chromedriver", chrome_options=self.chrome_options
        )
        self.site_url = site_url
        self.driver.get(self.site_url)

    def element_by_class_name_exists(
        self, class_name: str, time_to_wait: int = 10
    ) -> bool:
        """
        Checking element existing by class name
        :param class_name: Name of XML class
        :param time_to_wait: Time for waiting for element
        :return: Bool result value
        """
        try:
            logger.info(
                f"Checking presence of element existing with class name = {class_name} was initialized"
            )
            WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name))
            )
            logger.info(f"Element with class name = {class_name} exists on the page")
            return True
        except TimeoutException:
            logger.error(
                f"Checking presence of element existing with class name = {class_name} time out"
            )
            return False
        except Exception as excp:
            logger.error(
                f"Element with class name = {class_name} doesn't exist on the site with something went wrong because of {excp}"
            )
            return False

    def element_by_link_text_exists(
        self, link_text: str, time_to_wait: int = 10
    ) -> bool:
        """
        Checking element existing by class name
        :param class_name: Name of XML class
        :param time_to_wait: Time for waiting for element
        :return: Bool value
        """
        try:
            logger.info(
                f"Checking presence of element existing with link_text = {link_text} was initialized"
            )
            WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_text))
            )
            logger.info(f"Element with class name = {link_text} exists on the page")
            return True
        except TimeoutException:
            logger.error(f"Checking presence of element existing with link text = {link_text} time out")
            return False
        except Exception as excp:
            logger.error(
                f"Element with link text = {link_text} doesn't exist on the site with something went wrong because of {excp}"
            )
            return False

    def click_element_by_class_name(self, class_name: str, time_to_wait: int = 10):
        """
        Clicking on element existing by class name
        :param class_name: Name of XML class
        :param time_to_wait: Waiting time for the element appearing
        """
        try:
            logger.info(
                f"Clicking on the element with class name = {class_name} was initialized"
            )
            WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((By.CLASS_NAME, class_name))
            ).click()
            logger.info(
                f"Clicking on the element with class name = {class_name} was successfully done"
            )
        except TimeoutException:
            logger.error(f"Checking presence of element existing with class name = {class_name} time out")
            return False
        except NoSuchElementException:
            logger.error(f"Element with class name = {class_name} doesn't exist on the site")
            return False
        except Exception as excp:
            logger.error(
                f"Element with class name = {class_name} doesn't exist on the site page with something went wrong because of {excp}"
            )
            return False

    def click_element_by_x_path(self, x_path: str, time_to_wait: int = 10):
        """
        :param x_path: XPATH of the element
        :param time_to_wait: Waiting time for the element appearing
        """
        try:
            logger.info(f"Clicking on the element with x_path = {x_path} was initialized")
            WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((By.XPATH, x_path))
            ).click()
            logger.info(f"Clicking on the element with x_path = {x_path} was successfully done")
        except TimeoutException:
            logger.error(f"Checking presence of element existing with x_path = {x_path} time out")
            return False
        except NoSuchElementException:
            logger.error(f"Element with x_path = {x_path} doesn't exist on the site")
            return False
        except Exception as excp:
            logger.error(
                f"Element with x_path = {x_path} doesn't exist on the site with something went wrong because of {excp}"
            )
            return False

    def click_element_by_link_text(self, link_text: str, time_to_wait: int = 10):
        try:
            logger.info(f"Clicking on the element with link text = {link_text} was initialized")
            WebDriverWait(self.driver, time_to_wait).until(
                EC.presence_of_element_located((By.LINK_TEXT, link_text))
            ).click()
            logger.info(
                f"Clicking on the element with link text = {link_text} was successfully done"
            )
        except TimeoutException:
            logger.error(
                f"Checking presence of element existing with link text = {link_text} time out"
            )
            return False
        except NoSuchElementException:
            logger.error(f"Element with link text = {link_text} doesn't exist on the site")
            return False
        except Exception as excp:
            logger.error(
                f"Element with link text = {link_text} doesn't exist on the site with something went wrong because of {excp}"
            )
            return False

    def get_source_html_with_url_prefix(self, url_prefix: str):
        """
        Getting the Source html base
        :param valute: Converting type from one valute to another element
        :return: New page object
        """
        logger.info(f"Entering to the new page of  {self.site_url} with url_prefix = {url_prefix} was initialized")
        new_page = self.driver.get(self.site_url + url_prefix)
        logger.info(
            "The new source page entering was successfully done.\n3-seconds waiting for another actions was initialized"
        )
        time.sleep(3)
        return new_page

    def get_source_html(self):
        """
        Getting the html code page source
        :return: Source page in html
        """
        logger.info("Getting the html code page source")
        return self.driver.page_source

    def quit(self):
        """
        Selenium quit
        """
        logger.info("Selenium object quit")
        self.driver.quit()
