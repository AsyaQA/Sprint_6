import pytest
import allure
from data import order_data_1, order_data_2
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Заказ самоката с двумя видами данных"')
    @pytest.mark.parametrize(
        'main_locator, name, last_name, address, phone_number, metro_station, day, period',
        [
            (MainPageLocators.ORDER_BUTTON_HEADER,
             order_data_1['name'],
             order_data_1['last_name'],
             order_data_1['address'],
             order_data_1['phone_number'],
             OrderPageLocators.METRO_1,
             order_data_1['day'],
             OrderPageLocators.RENTAL_PERIOD_1
             ),
            (MainPageLocators.ORDER_BUTTON_FOOTER,
             order_data_2['name'],
             order_data_2['last_name'],
             order_data_2['address'],
             order_data_2['phone_number'],
             OrderPageLocators.METRO_2,
             order_data_2['day'],
             OrderPageLocators.RENTAL_PERIOD_2
             )
        ]
    )
    def test_create_order(self, driver, main_locator, name, last_name, address, phone_number, metro_station, day, period):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_to_the_element(main_locator)
        order_page.find_element_with_wait(OrderPageLocators.NEXT_BUTTON)
        order_page.set_order(name, last_name, address, phone_number, metro_station, day, period)
        assert order_page.check_status() == "Посмотреть статус"