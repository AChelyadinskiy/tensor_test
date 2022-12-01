from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.images_page import ImagesPage
from pages.search_page import SearchPage


class MainPage(BasePage):
    SEARCH_FIELD_FRAME = (By.CLASS_NAME, "dzen-search-arrow-common__frame")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[name='text']")
    SUGGEST_TABLE = (By.CSS_SELECTOR, "div.mini-suggest__popup.mini-suggest__popup_svg_yes")
    YANDEX_IMAGES_LINK = (By.XPATH, "//span[contains(@class, 'desktop-services__icon desktop-services__icon_images')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://yandex.ru")

    def get_search_field(self) -> WebElement:
        """Returns searching field element on webpage"""
        self.driver.switch_to.default_content()
        frame = self.get_elem(self.SEARCH_FIELD_FRAME)
        self.driver.switch_to.frame(frame)
        search_field = self.get_elem(self.SEARCH_FIELD)
        return search_field

    def is_search_field_exist(self) -> bool:
        """Checks availability of searching field element on webpage"""
        try:
            self.get_search_field()
            return True
        except TimeoutException:
            return False

    def fill_search_field(self, text: str) -> None:
        """Inputs text to searching field"""
        self.get_search_field().send_keys(text)

    def is_suggest_table_exist(self) -> bool:
        """Checks availability of suggest table from searching field element on webpage"""
        return self.is_visible(self.SUGGEST_TABLE)

    def do_search(self) -> SearchPage:
        """Returns new page with results of searching"""
        count_window_handles = len(self.driver.window_handles)
        self.get_search_field().send_keys(Keys.ENTER)
        self.wait.until(ec.number_of_windows_to_be(count_window_handles + 1))
        self.switch_to_new_window_handle()
        return SearchPage(self.driver)

    def get_images_page_link(self) -> WebElement:
        """Returns element with link to Yandex.Images"""
        self.get_search_field().click()
        link = self.wait.until(ec.element_to_be_clickable(self.YANDEX_IMAGES_LINK))
        return link

    def is_images_page_link_exist(self) -> bool:
        """Checks availability of element with link to Yandex.Images on webpage"""
        try:
            self.get_images_page_link()
            return True
        except TimeoutException:
            return False

    def open_images_page(self) -> ImagesPage:
        """Returns page of Yandex.Images with founded images"""
        count_window_handles = len(self.driver.window_handles)
        self.get_images_page_link().click()
        self.wait.until(ec.number_of_windows_to_be(count_window_handles + 1))
        self.switch_to_new_window_handle()
        return ImagesPage(self.driver)
