from pages.base_page import BasePage
from utils.data import Urls
from utils.locators import LoginLocators


class LoginPage(BasePage):
    def open_login_page(self):
        self.open(Urls.BASE_URL)
        return self

    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        return self
        
    def enter_username(self, username):
        self.find(LoginLocators.USERNAME_INPUT).send_keys(username)
        return self

    def enter_password(self, password):
        self.find(LoginLocators.PASSWORD_INPUT).send_keys(password)
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self
        
    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)
    
    def is_login_page_displayed(self):
        return (
            self.is_visible(LoginLocators.LOGIN_CONTAINER) and
            self.is_visible(LoginLocators.LOGIN_BUTTON) and
            self.get_current_url() == Urls.BASE_URL
        )