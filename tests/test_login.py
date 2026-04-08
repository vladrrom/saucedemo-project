import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data import LoginData, Messages


@allure.epic("Тестирование страницы авторизации")
@pytest.mark.auth
class TestLogin:
    @allure.title("Успешная авторизация с действительными учетными данными")
    @allure.story("Позитивный тест на авторизацию")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_success_login(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login.open_login_page()
            
        with allure.step("Проверить, отображается ли страница входа"):
            assert login.is_login_page_displayed()
            
        with allure.step("Выполнить вход с действительными учетными данными"):
            login.login(LoginData.VALID_LOGIN, LoginData.VALID_PASSWORD)
            
        with allure.step("Проверить, загрузилась ли главная страница"):
            assert inventory.is_inventory_page_loaded()
        
        
    @allure.title("Ошибка авторизации с неправильным паролем")
    @allure.story("Негативный тест на авторизацию с неправильным паролем")
    @allure.severity(allure.severity_level.NORMAL)   
    def test_wrong_password(self, driver):
        login = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login.open_login_page()
            
        with allure.step("Проверить, отображается ли страница входа"):
            assert login.is_login_page_displayed()
            
        with allure.step("Выполнить вход с неправильным паролем"):
            login.login(LoginData.VALID_LOGIN, LoginData.WRONG_PASSWORD)
            
        with allure.step("Проверить сообщение об ошибке для недействительных учетных данных"):
            assert login.get_error_message() == Messages.ERROR_INVALID_CREDENTIALS


    @allure.title("Ошибка авторизации для заблокированного пользователя")
    @allure.story("Негативный тест на авторизацию для заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    def test_locked_user(self, driver):
        login = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login.open_login_page()
            
        with allure.step("Проверить, отображается ли страница входа"):
            assert login.is_login_page_displayed()
            
        with allure.step("Выполнить вход с заблокированным пользователем"):
            login.login(LoginData.LOCKED_LOGIN, LoginData.VALID_PASSWORD)
        
        with allure.step("Проверить сообщение об ошибке для заблокированного пользователя"):
            assert login.get_error_message() == Messages.ERROR_LOCKED_OUT
        
        
    @allure.title("Ошибка авторизации при пустых полях")
    @allure.story("Негативный тест на авторизацию с пустыми полями")
    @allure.severity(allure.severity_level.NORMAL)
    def test_empty_fields(self, driver):
        login = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login.open_login_page()
            
        with allure.step("Проверить, отображается ли страница входа"):
            assert login.is_login_page_displayed()
            
        with allure.step("Нажать кнопку входа без заполнения полей"):
            login.click_login_button()
        
        with allure.step("Проверить сообщение об ошибке для пустых полей"):
            assert login.get_error_message() == Messages.ERROR_USERNAME_REQUIRED
    
    @allure.title("Авторизация с пользователем-гличом")
    @allure.story("Позитивный тест на авторизацию с пользователем-гличом")
    @allure.severity(allure.severity_level.NORMAL)
    def test_glitch_user(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login.open_login_page()
            
        with allure.step("Проверить, отображается ли страница входа"):
            assert login.is_login_page_displayed()
            
        with allure.step("Выполнить вход с пользователем-гличом"):
            login.login(LoginData.GLITCH_LOGIN, LoginData.VALID_PASSWORD)
        
        with allure.step("Проверить, загрузилась ли главная страница"):
            assert inventory.is_inventory_page_loaded()