import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_EXEC_PATH = "C:/Drivers/chromedriver.exe"


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    service = Service(DRIVER_EXEC_PATH)
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=service)
    request.cls.driver = web_driver
    yield
    web_driver.close()
