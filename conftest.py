import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from data import url, add_cookie_locator


@pytest.fixture
def driver():
    firefox_options = Options()
    firefox_options.add_argument('-width=1920')
    firefox_options.add_argument('-height=1080')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    driver.find_element(*add_cookie_locator).click()
    yield driver
    driver.quit()