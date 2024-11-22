from locators.redirect_locators import RedirectPageLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):

    def redirect_to_dzen_page(self):
        self.click_to_the_element(RedirectPageLocators.YANDEX)

    def check_redirect_to_dzen_page(self):
        return self.find_element_with_wait(RedirectPageLocators.DZEN).text

    def redirect_to_main_page(self):
        self.click_to_the_element(RedirectPageLocators.SCOOTER_LOGO)

    def check_redirect_to_main_page(self, locator):
        return self.get_text_from_element(locator)




