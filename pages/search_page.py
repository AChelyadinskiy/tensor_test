from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    SEARCH_RESULT_TABLE = (By.ID, "search-result")
    FIRST_LINK = (By.XPATH, "(//li[contains(@class, 'serp-item serp-item_card')][1]//a)[2]/b")

    def is_search_result_table_exist(self) -> bool:
        """Checks availability of searching results on webpage"""
        return self.is_visible(self.SEARCH_RESULT_TABLE)

    def get_first_link_from_table(self) -> str:
        """Returns link on first site"""
        table = self.get_elem(self.SEARCH_RESULT_TABLE)
        links = table.find_elements(*self.FIRST_LINK)
        if links:
            return links[0].text
