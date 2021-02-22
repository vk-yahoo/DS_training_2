# -*- coding: utf-8 -*-
import os
import time
import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_add_product(driver):
    """
    Сделайте сценарий для добавления нового товара (продукта) в учебном приложении litecart (в админке).
    Для добавления товара нужно
        - открыть меню Catalog;
        - в правом верхнем углу нажать кнопку "Add New Product";
        - заполнить поля с информацией о товаре и сохранить.
    Достаточно заполнить только информацию на вкладках General, Information и Prices.
    Скидки (Campains) на вкладке Prices можно не добавлять.
    Переключение между вкладками происходит не мгновенно, поэтому после переключения можно сделать небольшую паузу
    (о том, как делать более правильные ожидания, будет рассказано в следующих занятиях).
    Картинку с изображением товара нужно уложить в репозиторий вместе с кодом.
    При этом указывать в коде полный абсолютный путь к файлу плохо, на другой машине работать не будет.
    Надо средствами языка программирования преобразовать относительный путь в абсолютный.
    После сохранения товара нужно убедиться, что он появился в каталоге (в админке).
    Клиентскую часть магазина можно не проверять.
    """
    rand = str(datetime.datetime.now().strftime("%f"))
    product_name = 'product_' + rand
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    # Open add product page
    driver.get('http://localhost/litecart/public_html/admin/?category_id=0&app=catalog&doc=edit_product')
    # Add data on "General" tab
    driver.find_element_by_css_selector('[type="radio"][value="1"]').click()
    driver.find_element_by_css_selector('[name="name[en]"]').send_keys(product_name)
    driver.find_element_by_css_selector('[name="code"]').send_keys(rand)
    driver.find_element_by_css_selector('[data-name="Root"]').click()
    driver.find_element_by_css_selector('[data-name="Rubber Ducks"]').click()
    driver.find_element_by_css_selector('[name="product_groups[]"][value="1-3"]').click()
    product_quantity = driver.find_element_by_css_selector('[name="quantity"]')
    product_quantity.clear()
    product_quantity.send_keys('100')

    # Add image
    driver.find_element_by_css_selector('[name="new_images[]"]').send_keys(os.getcwd() + "/001.jpg")

    driver.find_element_by_css_selector('[name="date_valid_from"]').send_keys(22022021)
    driver.find_element_by_css_selector('[name="date_valid_to"]').send_keys(31122021)

    # Add data on "Information" tab
    driver.find_element_by_css_selector('.index li:nth-child(2)').click()
    time.sleep(1)
    select_manufacturer = Select(driver.find_element_by_css_selector('[name="manufacturer_id"]'))
    select_manufacturer.select_by_visible_text("ACME Corp.")
    driver.find_element_by_css_selector('[name="keywords"]').send_keys('Keywords')
    driver.find_element_by_css_selector('[name="short_description[en]"]').send_keys('Short description')
    driver.find_element_by_css_selector('.trumbowyg-editor').send_keys('Long description')
    driver.find_element_by_css_selector('[name="head_title[en]"]').send_keys('Head title')
    driver.find_element_by_css_selector('[name="meta_description[en]"]').send_keys('Meta description')

    # Add data on "Information" tab
    driver.find_element_by_css_selector('.index li:nth-child(4)').click()
    time.sleep(1)

    purchase_price = driver.find_element_by_css_selector('[name="purchase_price"]')
    purchase_price.clear()
    purchase_price.send_keys('13')
    select_currency = Select(driver.find_element_by_css_selector('[name="purchase_price_currency_code"]'))
    select_currency.select_by_visible_text("Euros")

    driver.find_element_by_css_selector('[name="save"]').click()
    time.sleep(1)

    # Assert product was added
    # Variant 1
    catalog = driver.find_element_by_css_selector('[name="catalog_form"]')
    catalog.find_elements_by_xpath('//a[contains(text(), "%s")]' % product_name)

    # Variant 2
    assert product_name in driver.find_element_by_css_selector('[name="catalog_form"]').get_attribute("textContent")

    # Variant 3
    elements = driver.find_elements_by_css_selector('[name="catalog_form"] a')
    for element in elements:
        if element.get_attribute("textContent") == product_name:
            print(element)
