from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open(self):
        self.open(self.URL)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        
    def enter_username(self, username):
        self.find(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.find(self.PASSWORD_INPUT).send_keys(password)
        
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)