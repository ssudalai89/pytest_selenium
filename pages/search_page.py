from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_box = (By.NAME, "q")
        self.search_results = (By.ID, "search")
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)
        # Wait for search box to be visible
        self.wait.until(EC.visibility_of_element_located(self.search_box))

    def search_for(self, text):
        search_input = self.wait.until(EC.element_to_be_clickable(self.search_box))
        search_input.clear()
        search_input.send_keys(text)
        search_input.send_keys(Keys.RETURN)
        # Wait for results to load
        self.wait.until(EC.presence_of_element_located(self.search_results))
    
    def get_title(self):
        # Get the page source and check if our search term is in it
        return self.driver.page_source
