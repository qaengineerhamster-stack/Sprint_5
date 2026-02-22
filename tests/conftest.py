import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture
def base_url():
    return "https://stellarburgers.education-services.ru/"


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser_name):
    if browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("-headless")  # чтобы видеть браузер — закомментируй
        drv = webdriver.Firefox(options=options)
    else:
        options = ChromeOptions()
        options.add_argument("--headless=new")  # чтобы видеть браузер — закомментируй
        options.add_argument("--window-size=1280,900")
        drv = webdriver.Chrome(options=options)

    yield drv
    drv.quit()