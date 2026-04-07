from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

class TestLogin:
    def test_success_login(driver):
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        assert inventory.is_opened()
        
