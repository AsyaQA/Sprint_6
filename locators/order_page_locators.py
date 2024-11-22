from selenium.webdriver.common.by import By


class OrderPageLocators:

    NEXT_BUTTON = By.XPATH, '//div[contains(@class, "Order_NextButton")]/button[contains(@class, "Button_Button")]'
    NAME = By.XPATH, '//*[@placeholder="* Имя"]'
    LAST_NAME = By.XPATH, '//*[@placeholder="* Фамилия"]'
    ADDRESS = By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_STATION = By.XPATH, '//*[@placeholder="* Станция метро"]'
    METRO_1 = By.XPATH, '//button[@value="4"]'
    METRO_2 = By.XPATH, '//button[@value="9"]'
    PHONE_NUMBER = By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]'
    WHERE = By.XPATH, '//*[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_FIELD = By.XPATH, '//span[@class="Dropdown-arrow"]'
    RENTAL_PERIOD_1 = By.XPATH, '//*[text()="четверо суток"]'
    RENTAL_PERIOD_2 = By.XPATH, '//*[text()="сутки"]'
    FINISH_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]'
    CONFIRM_ORDER = By.XPATH, '//*[text()="Да"]'
    CHECK_STATUS = By.XPATH, '//*[text()="Посмотреть статус"]'
    CHECK_ORDER_TEXT = By.XPATH, '//*[text()="Для кого самокат"]'
