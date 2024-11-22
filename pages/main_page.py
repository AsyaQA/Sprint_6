from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_to_the_order_button_header(self):
        self.click_to_the_element(MainPageLocators.ORDER_BUTTON_HEADER)

    def get_accordion_list(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        self.scroll_to_the_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.click_to_the_element(locator_q_formatted)
        return self.get_text_from_element(locator_a_formatted)










