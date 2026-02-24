import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    # Если нужно видеть браузер — оставь так.
    # Если нужно headless — раскомментируй:
    # options.add_argument("--headless=new")

    options.add_argument("--window-size=1280,900")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()