# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.support.color import Color


@pytest.fixture
def driver(request):
    # wd = webdriver.Chrome()

    # wd = webdriver.Firefox(firefox_binary="c:\\Program Files\\Mozilla Firefox\\firefox.exe")

    wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    return wd


def test_check_product_page(driver):
    """
    Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара
    в учебном приложении litecart.
    Нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:
        а) на главной странице и на странице товара совпадает текст названия товара
        б) на главной странице и на странице товара совпадают цены (обычная и акционная)
        в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой,
            у которого в RGBa представлении одинаковые значения для каналов R, G и B)
        г) акционная жирная и красная (можно считать, что "красный" цвет это такой,
            у которого в RGBa представлении каналы G и B имеют нулевые значения)
            (цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
        д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)

        Убедиться, что тесты работают в разных браузерах (Chrome, Firefox, IE).
    """

    driver.get('http://localhost/litecart/public_html')
    product_hp = driver.find_element_by_css_selector('#box-campaigns .product')
    name_hp = product_hp.find_element_by_css_selector('.name').get_attribute('textContent')
    sticker_hp = product_hp.find_element_by_css_selector('.sticker').get_attribute('textContent')
    regular_price_hp = product_hp.find_element_by_css_selector('.regular-price').get_attribute('textContent')
    reg_price_hp_color = product_hp.find_element_by_css_selector('.regular-price').value_of_css_property('color')
    reg_price_hp_style = product_hp.find_element_by_css_selector(
        '.regular-price').value_of_css_property('text-decoration')
    reg_price_hp_size = product_hp.find_element_by_css_selector(
        '.regular-price').value_of_css_property('font-weight')
    sale_price_hp = product_hp.find_element_by_css_selector('.campaign-price').get_attribute('textContent')
    sale_price_hp_color = product_hp.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
    sale_price_hp_size = product_hp.find_element_by_css_selector(
        '.campaign-price').value_of_css_property('font-weight')

    driver.find_element_by_css_selector('#box-campaigns .product a.link').click()
    product_pp = driver.find_element_by_css_selector('#box-product')
    name_pp = product_pp.find_element_by_css_selector('.title').get_attribute('textContent')
    sticker_pp = product_pp.find_element_by_css_selector('.sticker').get_attribute('textContent')
    regular_price_pp = product_pp.find_element_by_css_selector('.regular-price').get_attribute('textContent')
    reg_price_pp_color = product_pp.find_element_by_css_selector('.regular-price').value_of_css_property('color')
    reg_price_pp_style = product_pp.find_element_by_css_selector(
        '.regular-price').value_of_css_property('text-decoration')
    reg_price_pp_size = product_pp.find_element_by_css_selector(
        '.regular-price').value_of_css_property('font-weight')
    sale_price_pp = product_pp.find_element_by_css_selector('.campaign-price').get_attribute('textContent')
    sale_price_pp_color = product_pp.find_element_by_css_selector('.campaign-price').value_of_css_property('color')
    sale_price_pp_size = product_pp.find_element_by_css_selector(
        '.campaign-price').value_of_css_property('font-weight')

    # Check titles
    assert name_hp == name_pp
    # Check stickers
    assert sticker_hp == sticker_pp
    # Check regular price
    assert regular_price_hp == regular_price_pp
    # Check sale price
    assert sale_price_hp == sale_price_pp
    # Check that regular price is gray on home page and product page
    assert Color.from_string(reg_price_hp_color).red == Color.from_string(
        reg_price_hp_color).green == Color.from_string(reg_price_hp_color).blue
    assert Color.from_string(reg_price_pp_color).red == Color.from_string(
        reg_price_pp_color).green == Color.from_string(reg_price_pp_color).blue
    # Check that sale price is red on home page and product page
    assert Color.from_string(sale_price_hp_color).red != 0 and Color.from_string(
        sale_price_hp_color).green == Color.from_string(sale_price_hp_color).blue == 0
    assert Color.from_string(sale_price_pp_color).red != 0 and Color.from_string(
        sale_price_pp_color).green == Color.from_string(sale_price_pp_color).blue == 0
    # Check that regular price is crossed out on home page and product page
    assert 'line-through' in reg_price_hp_style
    assert 'line-through' in reg_price_pp_style
    # Check that sale price is bold on home page and product page
    assert reg_price_hp_size == reg_price_pp_size == '400'
    # Check that sale price is bold on home page and product page
    assert sale_price_hp_size == '700' or sale_price_hp_size == '900'
    assert sale_price_pp_size == '700'


# def test_check_product_pages_all(driver):
#     driver.get('http://localhost/litecart/public_html')
#     for x in range(len(driver.find_elements_by_class_name('product'))):
#         price1 = price2 = price3 = product_price1 = product_price2 = product_price3 = None
#         driver.get('http://localhost/litecart/public_html')
#         products_list = driver.find_elements_by_class_name('product')
#         name = products_list[x].find_element_by_css_selector('.name').get_attribute('textContent')
#         sticker = products_list[x].find_element_by_css_selector('.sticker').get_attribute('textContent')
#         price = products_list[x].find_elements_by_css_selector('.price')
#         if len(price) > 0:
#             price1 = price[0].get_attribute('textContent')
#         regular_price = products_list[x].find_elements_by_css_selector('.regular-price')
#         if len(regular_price) > 0:
#             price2 = regular_price[0].get_attribute('textContent')
#         campaign_price = products_list[x].find_elements_by_css_selector('.campaign-price')
#         if len(campaign_price) > 0:
#             price3 = campaign_price[0].get_attribute('textContent')
#         img_alt_text = products_list[x].find_element_by_css_selector('img').get_attribute('alt')
#         products_list[x].click()
#         product_page = driver.find_element_by_css_selector('#box-product')
#         product_title = product_page.find_element_by_css_selector('.title').get_attribute('textContent')
#         product_sticker = product_page.find_element_by_css_selector('.sticker').get_attribute('textContent')
#         product_price = product_page.find_elements_by_css_selector('.price')
#         if len(product_price) > 0:
#             product_price1 = product_price[0].get_attribute('textContent')
#         product_regular_price = product_page.find_elements_by_css_selector('.regular-price')
#         if len(product_regular_price) > 0:
#             product_price2 = product_regular_price[0].get_attribute('textContent')
#         product_campaign_price = product_page.find_elements_by_css_selector('.campaign-price')
#         if len(product_campaign_price) > 0:
#             product_price3 = product_campaign_price[0].get_attribute('textContent')
#         product_img_alt_text = product_page.find_element_by_css_selector('img').get_attribute('alt')
#
#         assert name == product_title
#         assert sticker == product_sticker
#         assert price1 == product_price1
#         assert price2 == product_price2
#         assert price3 == product_price3
#         assert img_alt_text == product_img_alt_text
