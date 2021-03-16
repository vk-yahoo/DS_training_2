import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        print(by, value)

    def after_find(self, by, value, driver):
        print(by, value, "found")

    def on_exception(self, exception, driver):
        print(exception)


@pytest.fixture
def driver(request):
    wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get('http://www.google.com')
    driver.find_element_by_name('btnK')
    driver.get_screenshot_as_file('screen0.png')
    driver.find_element_by_name('nbtnI')
    driver.get_screenshot_as_file('screen1.png')

    driver.find_element_by_name('q').send_keys('webdriver')
    driver.find_element_by_name('q').send_keys(Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.title_contains('webdriver'))
