# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def browser_logs(driver):
    logs = driver.get_log("browser")
    if logs:
        for log in logs:
            print(log)
    else:
        print('\nNo browser logs available')


def test_admin_add_product(driver):
    """
    Сделайте сценарий, который проверяет, не появляются ли в логе браузера сообщения
    при открытии страниц в учебном приложении, а именно - страниц товаров в каталоге в административной панели.

    Сценарий должен состоять из следующих частей:
    1) зайти в админку
    2) открыть каталог, категорию, которая содержит товары
    (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
    3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения
    """

    # Login to the admin
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    # Open the Catalog page
    driver.get('http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog&category_id=1')

    # Open every available product page
    products_count = len(driver.find_elements_by_css_selector('[title="Edit"]'))

    for i in range(2, products_count):
        driver.find_elements_by_css_selector('[title="Edit"]')[i].click()
        driver.find_element_by_css_selector('button[name="save"]')
        browser_logs(driver)
        driver.get('http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog&category_id=1')

    # Logs for scoperty.de
    driver.get('https://scoperty.de/home')
    browser_logs(driver)
