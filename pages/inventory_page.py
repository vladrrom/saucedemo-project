import allure
from pages.base_page import BasePage
from utils.data import Urls
from utils.locators import InventoryLocators


class InventoryPage(BasePage):
    @allure.step("Проверить, загрузилась ли главная страница")
    def is_inventory_page_loaded(self):
        return (
            self.is_visible(InventoryLocators.INVENTORY_CONTAINER) and
            self.is_visible(InventoryLocators.PRODUCT_TITLE) and
            self.get_current_url() == Urls.INVENTORY_URL
        )