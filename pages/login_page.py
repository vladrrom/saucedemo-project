from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    LOGIN_CONTAINER = (By.ID, "login_button_container")
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    def open_login_page(self):
        self.open(self.URL)
        return self

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
        return self
        
    def enter_username(self, username):
        self.find(self.USERNAME_INPUT).send_keys(username)
        return self

    def enter_password(self, password):
        self.find(self.PASSWORD_INPUT).send_keys(password)
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self
        
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_login_page_displayed(self):
        return (
            self.is_visible(self.LOGIN_CONTAINER) and
            self.is_visible(self.LOGIN_BUTTON) and
            self.get_current_url() == self.URL
        )