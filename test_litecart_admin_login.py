import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    # Chrome
    # wd = webdriver.Chrome()

    # Firefox
    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")

    # Firefox 45.0.1esr
    # wd = webdriver.Firefox(
    #     capabilities={"marionette": False},
    #     firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe"
    # )

    # Firefox Nightly
    wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Firefox Nightly\\firefox.exe")

    # IE
    # wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
