import allure
from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.redirect_page import RedirectPage


class TestRedirectPage:

    @allure.title('Проверка перехода на Дзен"')
    def test_redirect_to_dzen(self, driver):
        redirect_page = RedirectPage(driver)
        redirect_page.redirect_to_dzen_page()
        redirect_page.switch_to_page(driver)
        assert redirect_page.check_redirect_to_dzen_page() == 'Найти'

    @allure.title('Проверка перехода на главную страницу приложения"')
    def test_redirect_to_main_page(self, driver):
        main_page_red = MainPage(driver)
        order_page_red = OrderPage(driver)
        redirect_page_red = RedirectPage(driver)
        main_page_red.click_to_the_order_button_header()
        order_page_red.find_element_with_wait(OrderPageLocators.CHECK_ORDER_TEXT)
        redirect_page_red.redirect_to_main_page()
        assert 'Самокат' in redirect_page_red.check_redirect_to_main_page(MainPageLocators.SCOOTER_TEXT)