from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def get_current_url(self) -> str:
        """Returns url of current page"""
        return self.driver.current_url

    def get_elem(self, by_locator: tuple[By, str]) -> WebElement:
        """Returns element of webpage by selected locator"""
        return self.wait.until(ec.visibility_of_element_located(by_locator))

    def is_visible(self, by_locator: tuple[By, str]) -> bool:
        """Check visibility of element on webpage"""
        try:
            self.get_elem(by_locator)
        except TimeoutException:
            return False
        return True

    def switch_to_new_window_handle(self) -> None:
        """Switch active window handle to last opened"""
        self.driver.switch_to.window(self.driver.window_handles[-1])
