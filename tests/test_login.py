from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:
    def test_success_login(driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        assert inventory.is_opened()
        
        
    def test_wrong_password(driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "123456")

        assert login.get_error_message() == "Epic sadface: Username and password do not match any user in this service"
        
    
    def test_locked_user(driver):
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        
        assert login.get_error_message() == "Epic sadface: Sorry, this user has been locked out."
        
        
    def test_empty_fields(driver):
        login = LoginPage(driver)
        login.open()
        login.click_login()
        
        assert login.get_error_message() == "Epic sadface: Username is required"