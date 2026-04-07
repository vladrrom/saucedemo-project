from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:
    def test_success_login(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login("standard_user", "secret_sauce")

        assert inventory.is_inventory_page_loaded()
        
        
    def test_wrong_password(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login("standard_user", "123456")

        assert login.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
        
    
    def test_locked_user(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login("locked_out_user", "secret_sauce")
        
        assert login.get_error_message() == "Epic sadface: Sorry, this user has been locked out."
        
        
    def test_empty_fields(self, driver):
        login = LoginPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.click_login_button()
        
        assert login.get_error_message() == "Epic sadface: Username is required"
    
    
    def test_glitch_user(self, driver):
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        
        login.open_login_page()
        login.is_login_page_displayed()
        login.login("performance_glitch_user", "secret_sauce")
        
        assert inventory.is_inventory_page_loaded()