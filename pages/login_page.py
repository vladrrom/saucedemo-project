import allure
from pages.base_page import BasePage
from utils.data import Urls
from utils.locators import LoginLocators


class LoginPage(BasePage):
    @allure.step("Открыть страницу логина")
    def open_login_page(self):
        self.open(Urls.BASE_URL)
        return self

    @allure.step("Нажать на кнопку входа")
    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username):
        self.find(LoginLocators.USERNAME_INPUT).send_keys(username)
        return self

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.find(LoginLocators.PASSWORD_INPUT).send_keys(password)
        return self

    @allure.step("Выполнить вход с именем пользователя: {username} и паролем: {password}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        return self
        
    @allure.step("Получить сообщение об ошибке входа")
    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)
    
    @allure.step("Проверить, отображается ли страница входа")
    def is_login_page_displayed(self):
        return (
            self.is_visible(LoginLocators.LOGIN_CONTAINER) and
            self.is_visible(LoginLocators.LOGIN_BUTTON) and
            self.get_current_url() == Urls.BASE_URL
        )