import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_sections(driver):
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()
    admin_sections_count = len(driver.find_elements_by_css_selector('#app-'))
    for x in range(admin_sections_count):
        driver.find_elements_by_css_selector('#app- > a')[x].click()
    print('\nI have visited every of ' + str(admin_sections_count) + ' admin sections!')


def test_check_product_stickers(driver):
    driver.get('http://localhost/litecart/public_html')
    products_list = driver.find_elements_by_class_name('product')
    for product in products_list:
        product.find_element_by_class_name('sticker')
    print('\nEvery of ' + str(len(products_list)) + ' ducks has a sticker!')
