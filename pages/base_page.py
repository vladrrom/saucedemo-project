import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from utils.data import Timeouts

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Timeouts.EXPLICIT_WAIT)

    @allure.step("Открыть страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент: {locator}")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Нажать на элемент: {locator}")
    def click(self, locator):
        return self.find(locator).click()
        
    @allure.step("Получить текст из элемента: {locator}")
    def get_text(self, locator):
        return self.find(locator).text
    
    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator):
        try: 
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url