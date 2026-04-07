import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument("--window-size=1440,1080")
    options.add_argument("--headless")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    
    attach = driver.get_screenshot_as_png()
    allure.attach(
        attach,
        name=f"Screenshot {datetime.today}",
        attachment_type=allure.attachment_type.PNG,
    )
    allure.attach(
        driver.page_source,
        name=f"Page {datetime.today}",
        attachment_type=allure.attachment_type.HTML,
    )
    
    driver.quit()