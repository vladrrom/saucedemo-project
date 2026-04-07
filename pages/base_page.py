from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    timeout = 10
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        return self.find(locator).click()
        
    def get_text(self, locator):
        return self.find(locator).text
    
    def is_visible(self, locator):
        try: 
            self.wait.until(EC.visibility_of_element_located(locator))
            return self
        except TimeoutException:
            return False
    
    def get_current_url(self):
        return self.driver.current_url