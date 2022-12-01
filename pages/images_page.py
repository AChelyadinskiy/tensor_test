from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec


class ImagesPage(BasePage):
    FIRST_CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item.PopularRequestList-Item_pos_0")
    IMAGE_SEARCH_INPUT = (By.CSS_SELECTOR, "input.input__control")
    FIRST_IMAGE = (By.CSS_SELECTOR, ".serp-item_pos_0")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next i.CircleButton-Icon")
    BUTTON_PREV = (By.CSS_SELECTOR, ".CircleButton_type_prev i.CircleButton-Icon")
    IMAGE_PREVIEW = (By.CSS_SELECTOR, "img.MMImage-Preview")

    def get_first_category(self) -> WebElement:
        """Returns web element of first category on Yandex.Images """
        return self.get_elem(self.FIRST_CATEGORY)

    def get_first_category_name(self) -> str:
        """Returns name of first category on Yandex.Images"""
        first_category = self.get_first_category()
        if first_category:
            return first_category.get_attribute("innerText")

    def select_first_category(self) -> None:
        """Select first category on Yandex.Images"""
        self.get_first_category().click()

    def get_image_search_input(self) -> str:
        """Returns text from searching field"""
        result = self.get_elem(self.IMAGE_SEARCH_INPUT)
        if result:
            return result.get_attribute("value")

    def open_first_image(self) -> None:
        """Opens first image on webpage"""
        image = self.get_elem(self.FIRST_IMAGE)
        image.click()

    def is_image_preview_exist(self) -> bool:
        """Check if image opened"""
        return self.is_visible(self.IMAGE_PREVIEW)

    def get_image_src(self) -> str:
        """Returns src attribute of element of current image """
        return self.get_elem(self.IMAGE_PREVIEW).get_attribute("src")

    def press_button_next(self) -> None:
        """"Switches to next image"""
        self.wait.until(ec.element_to_be_clickable(self.BUTTON_NEXT)).click()

    def press_button_prev(self) -> None:
        """Switches to previous image"""
        self.wait.until(ec.element_to_be_clickable(self.BUTTON_PREV)).click()
