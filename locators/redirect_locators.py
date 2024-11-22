from selenium.webdriver.common.by import By


class RedirectPageLocators:
    YANDEX = By.XPATH, '//img[@alt="Yandex"]'
    DZEN = By.XPATH, '//*[text()="Найти"]'
    SCOOTER_LOGO = By.XPATH, '//img[@alt="Scooter"]'
