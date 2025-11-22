import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Configure logging (can be moved to framework-level config)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class HomePage:
    def __init__(self,driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        
    def title_validation(self,expected_title):
        try:
            self.wait.until(EC.title_is(expected_title))
            actual_title = self.driver.title
            logging.info(f"Actual title: {actual_title}, Expected title: {expected_title}")
            assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}', but got '{actual_title}'"
            logging.info("Title validation passed.")
        except TimeoutException:
            logging.error(f"Title did not match expected '{expected_title}' within the timeout period.")
            raise
        except AssertionError as e:
            logging.error(str(e))
            raise

        
            


