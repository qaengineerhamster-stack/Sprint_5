from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.locators import MainPageLocators


def test_constructor_buns_tab_default(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER))


def test_constructor_sauces_tab(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.SAUCES_TAB)).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.SAUCES_HEADER))


def test_constructor_fillings_tab(driver, base_url):
    driver.get(base_url)
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.FILLINGS_TAB)).click()
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(MainPageLocators.FILLINGS_HEADER))