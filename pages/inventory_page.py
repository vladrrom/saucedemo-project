from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_URL = "https://www.saucedemo.com/inventory.html"
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    PRODUCT_TITLE = (By.CLASS_NAME, "title")

    def is_inventory_page_loaded(self):
        return (
            self.is_visible(self.INVENTORY_CONTAINER) and
            self.is_visible(self.PRODUCT_TITLE) and
            self.get_current_url() == self.INVENTORY_URL
        )
    
    def get_title(self):
        return self.get_text(self.PRODUCT_TITLE)