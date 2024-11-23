from selenium.webdriver.common.by import By


class MainPageLocators:

    ORDER_BUTTON_HEADER = By.XPATH, '//div[contains(@class, "Header_Nav")]/button[contains(@class, "Button_Button")]'
    ORDER_BUTTON_FOOTER = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[contains(@class, "Button_Button")]'
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]/p'
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]'
    SCOOTER_TEXT = By.XPATH, '//div[contains(@class, "Home_Header")]'