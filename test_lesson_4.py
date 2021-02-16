# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_sections(driver):
    """
    Сделайте сценарий, который выполняет следующие действия в учебном приложении litecart.
    1) входит в панель администратора http://localhost/litecart/admin
    2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
    3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)
    """
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    admin_sections_count = len(driver.find_elements_by_css_selector('#app-'))
    driver.refresh()
    for x in range(admin_sections_count):
        menu_items = driver.find_elements_by_css_selector('#app-')
        menu_items[x].click()
        driver.find_element_by_tag_name('h1')
        sub_menu_items_count = len(driver.find_elements_by_css_selector('#app-')[x].find_elements_by_css_selector('a'))
        if sub_menu_items_count > 2:
            for y in range(2, sub_menu_items_count):
                menu_items = driver.find_elements_by_css_selector('#app-')
                sub_menu_items = menu_items[x].find_elements_by_css_selector('a')
                sub_menu_items[y].click()
                driver.find_element_by_tag_name('h1')
    print('\nI have visited every of ' + str(admin_sections_count) + ' admin sections with all subsections!')


def test_check_product_stickers(driver):
    """
    Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
    Стикеры -- это полоски в левом верхнем углу изображения товара,
    на которых написано New или Sale или что-нибудь другое.
    Сценарий должен проверять, что у каждого товара имеется ровно один стикер.
    """
    driver.get('http://localhost/litecart/public_html')
    products_list = driver.find_elements_by_class_name('product')
    for product in products_list:
        product.find_element_by_class_name('sticker')
    print('\nEvery of ' + str(len(products_list)) + ' ducks has a sticker!')
