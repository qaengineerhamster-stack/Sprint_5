from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers import register_user, login
from locators import MainPageLocators


def test_from_profile_to_constructor_by_constructor_link(driver):
    email, password = register_user(driver)
    login(driver, email, password)

    # переходим в профиль
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
    ).click()

    # из профиля переходим в конструктор
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB)
    ).click()

    # проверяем, что мы на главной (виден заголовок "Булки")
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(MainPageLocators.BUNS_HEADER)
    )

    assert driver.find_element(*MainPageLocators.BUNS_HEADER).is_displayed()