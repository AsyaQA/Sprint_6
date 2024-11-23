import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage


class TestRedirectPage:

    @allure.title('Проверка перехода на Дзен"')
    def test_redirect_to_dzen(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.redirect_to_dzen_page()
        redirect_page.switch_to_page(driver)
        assert redirect_page.control_redirect_to_dzen_page() == 'Найти'

    @allure.title('Проверка перехода на главную страницу приложения"')
    def test_redirect_to_main_page(self, driver):
        main_page_red = MainPage(driver)
        order_page_red = OrderPage(driver)
        redirect_page_red = RedirectPage(driver)
        main_page_red.click_to_the_order_button_header()
        order_page_red.control_text_in_order_page()
        redirect_page_red.redirect_to_main_page()
        assert 'Самокат' in main_page_red.control_text_in_main_page()