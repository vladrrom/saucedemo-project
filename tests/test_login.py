from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.data import LoginData, Messages


class TestLogin:
    def test_success_login(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login(LoginData.VALID_LOGIN, LoginData.VALID_PASSWORD)

        assert inventory.is_inventory_page_loaded()
        
        
    def test_wrong_password(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login(LoginData.VALID_LOGIN, LoginData.WRONG_PASSWORD)

        assert login.get_error_message() == Messages.ERROR_INVALID_CREDENTIALS

    def test_locked_user(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login(LoginData.LOCKED_LOGIN, LoginData.VALID_PASSWORD)
        
        assert login.get_error_message() == Messages.ERROR_LOCKED_OUT
        
        
    def test_empty_fields(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.click_login_button()
        
        assert login.get_error_message() == Messages.ERROR_USERNAME_REQUIRED
    
    
    def test_glitch_user(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login(LoginData.GLITCH_LOGIN, LoginData.VALID_PASSWORD)
        
        assert inventory.is_inventory_page_loaded()