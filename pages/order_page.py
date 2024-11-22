from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def set_order(self, name, last_name, address, phone_number, metro_station, day, period):
        self.add_text_in_element(OrderPageLocators.NAME, name)
        self.add_text_in_element(OrderPageLocators.LAST_NAME, last_name)
        self.add_text_in_element(OrderPageLocators.ADDRESS, address)
        self.click_to_the_element(OrderPageLocators.METRO_STATION)
        self.click_to_the_element(metro_station)
        self.add_text_in_element(OrderPageLocators.PHONE_NUMBER, phone_number)
        self.click_to_the_element(OrderPageLocators.NEXT_BUTTON)
        self.find_element_with_wait(OrderPageLocators.FINISH_ORDER_BUTTON)
        self.add_text_in_element(OrderPageLocators.WHERE, day)
        self.click_to_the_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.click_to_the_element(period)
        self.click_to_the_element(OrderPageLocators.FINISH_ORDER_BUTTON)
        self.click_to_the_element(OrderPageLocators.CONFIRM_ORDER)

    def check_status(self):
        return self.get_text_from_element(OrderPageLocators.CHECK_STATUS)

