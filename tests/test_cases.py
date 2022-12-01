import pytest
from pages.main_page import MainPage


@pytest.mark.usefixtures("init_driver")
class TestCases:
    def test_yandex_search_tensor(self):
        main_page = MainPage(self.driver)
        expected_url = "https://dzen.ru/?yredirect=true"
        current_url = main_page.get_current_url()
        assert current_url == expected_url, f"not equal urls"
        assert main_page.is_search_field_exist() is True, "SEARCH_FIELD on main_page not found"

        main_page.fill_search_field("тензор")
        assert main_page.is_suggest_table_exist() is True, "SUGGEST_TABLE on main_page not found"

        search_page = main_page.do_search()
        assert search_page.is_search_result_table_exist() is True, "SEARCH_RESULT_TABLE on search_page not found"

        expected_link = "tensor.ru"
        current_link = search_page.get_first_link_from_table()
        assert current_link == expected_link, f"not equal links"

    def test_yandex_images(self):
        main_page = MainPage(self.driver)
        assert main_page.is_images_page_link_exist() is True, "IMAGES_PAGE_LINK on main_page not found"

        images_page = main_page.open_images_page()
        current_url = images_page.get_current_url()
        assert current_url.startswith("https://yandex.ru/images"), f"invalid url {current_url}"

        first_category_name = images_page.get_first_category_name()
        images_page.select_first_category()
        search_image_input_text = images_page.get_image_search_input()
        assert first_category_name == search_image_input_text, "category_name not equal"

        images_page.open_first_image()
        assert images_page.is_image_preview_exist() is True, "image isn't opened"

        image_1_src = images_page.get_image_src()
        images_page.press_button_next()
        image_2_src = images_page.get_image_src()
        assert image_1_src != image_2_src, "images are equal after 1 move"

        images_page.press_button_prev()
        assert images_page.get_image_src() == image_1_src, "images are not equal after 2 moves"
