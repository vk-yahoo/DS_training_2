# -*- coding: utf-8 -*-
from selenium.webdriver.support.color import Color


def test_check_product_page(app):
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

    app.open_application()

    home_page_product = app.app_main_page.get_campaigns_product_details_hp()
    app.app_main_page.open_product()
    product_page_product = app.app_main_page.get_campaigns_product_details_pp()

    # Check titles
    assert home_page_product["title"] == product_page_product["title"]

    # Check stickers
    assert home_page_product["sticker"] == product_page_product["sticker"]

    # Check regular price
    assert home_page_product["price"] == product_page_product["price"]

    # Check sale price campaign-price
    assert home_page_product["campaign-price"] == product_page_product["campaign-price"]

    # Check that regular price is gray on home page and product page
    assert Color.from_string(home_page_product["price color"]).red == Color.from_string(
        home_page_product["price color"]).green == Color.from_string(home_page_product["price color"]).blue
    assert Color.from_string(product_page_product["price color"]).red == Color.from_string(
        product_page_product["price color"]).green == Color.from_string(product_page_product["price color"]).blue

    # Check that sale price is red on home page and product page
    assert Color.from_string(home_page_product["campaign-price color"]).red != 0 and Color.from_string(
        home_page_product["campaign-price color"]).green == Color.from_string(
        home_page_product["campaign-price color"]).blue == 0
    assert Color.from_string(product_page_product["campaign-price color"]).red != 0 and Color.from_string(
        product_page_product["campaign-price color"]).green == Color.from_string(
        product_page_product["campaign-price color"]).blue == 0

    # Check that regular price is crossed out on home page and product page
    assert 'line-through' in home_page_product["price text-decoration"]
    assert 'line-through' in product_page_product["price text-decoration"]

    # Check that regular price is bold on home page and product page
    assert home_page_product["price font-weight"] == product_page_product["price font-weight"] == '400'

    # Check that sale price is bold on home page and product page
    assert home_page_product["campaign-price font-weight"] == '700' or home_page_product[
        "campaign-price font-weight"] == '900'
    assert product_page_product["campaign-price font-weight"] == '700'
