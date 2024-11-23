import pytest
import allure
from data import qa_dict
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверка списка "Вопросы о важном"')
    @pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_accordion_list(self, driver, num):
        main_page = MainPage(driver)
        assert main_page.get_accordion_list(num) == qa_dict[num]