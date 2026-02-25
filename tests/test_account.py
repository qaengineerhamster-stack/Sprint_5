from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators, ProfileLocators
from helpers import register_user, login, wait_page_loaded, wait_url_changed


class TestAccount:
    def test_open_personal_account(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        wait_page_loaded(driver)

        # реальный ассерт результата: мы в профиле и кнопка выхода есть
        assert "account" in driver.current_url
        assert len(driver.find_elements(*ProfileLocators.LOGOUT_BUTTON)) > 0

    def test_logout_from_profile(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        wait_page_loaded(driver)

        # нашли кнопку выхода (visibility достаточно)
        logout_btn = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(ProfileLocators.LOGOUT_BUTTON)
        )

        # на случай если обычный click не срабатывает (оверлей/слой)
        driver.execute_script("arguments[0].scrollIntoView(true);", logout_btn)

        old_url = driver.current_url
        driver.execute_script("arguments[0].click();", logout_btn)

        # нейтральное ожидание результата действия
        wait_url_changed(driver, old_url)
        wait_page_loaded(driver)

        # реальный ассерт: после выхода должны быть на login
        assert "login" in driver.current_url

    def test_from_profile_to_constructor_by_constructor_link(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_TAB)
        ).click()

        wait_page_loaded(driver)

        # реальный ассерт результата: вернулись в конструктор
        assert "account" not in driver.current_url

    def test_from_profile_to_constructor_by_logo(self, driver):
        email, password = register_user(driver)
        login(driver, email, password)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        ).click()

        wait_page_loaded(driver)

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        ).click()

        wait_page_loaded(driver)

        # реальный ассерт результата: ушли из личного кабинета
        assert "account" not in driver.current_url