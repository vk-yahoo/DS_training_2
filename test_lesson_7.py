# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_app_add_user(driver):
    """
    Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
    1. Открыть главную страницу
    2. Открыть первый товар из списка
    3. Добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
    4. Подождать, пока счётчик товаров в корзине обновится
    5. Вернуться на главную страницу, повторить предыдущие шаги ещё два раза,
    6. Открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
    7. Удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
    """

    wait = WebDriverWait(driver, 3)  # seconds
    driver.get('http://localhost/litecart/public_html')

    # Add products to a cart
    for i in range(1, 4):
        driver.find_elements_by_css_selector('.product')[0].click()
        wait.until(EC.text_to_be_present_in_element((By.ID, 'cart'), '%s item(s)' % (i-1)))
        if len(driver.find_elements_by_css_selector('[name="options[Size]"]')) == 1:
            select_size = Select(driver.find_element_by_css_selector('[name="options[Size]"]'))
            select_size.select_by_index(1)
        driver.find_element_by_css_selector('[name="add_cart_product"]').submit()
        wait.until(EC.text_to_be_present_in_element((By.ID, 'cart'), '%s item(s)' % i))
        driver.find_element_by_css_selector('#logotype-wrapper').click()
    driver.find_element_by_css_selector('#cart').click()

    # Remove products from the cart
    wait.until(EC.visibility_of_element_located((By.ID, 'box-checkout-summary')))
    cart_items = len(driver.find_elements_by_css_selector('td.item'))
    for i in range(cart_items-1):
        cart_box = driver.find_element_by_css_selector('#box-checkout-summary')
        item_mini_views = driver.find_elements_by_css_selector('a.act')
        ActionChains(driver).move_to_element(item_mini_views[0]).click_and_hold().release().perform()
        remove_buttons = driver.find_elements_by_css_selector('button[name="remove_cart_item"]')
        ActionChains(driver).move_to_element(remove_buttons[0]).click_and_hold().release().perform()
        wait.until(EC.invisibility_of_element(cart_box))
        assert len(driver.find_elements_by_css_selector('td.item')) == cart_items - i - 1
    remove_buttons = driver.find_elements_by_css_selector('button[name="remove_cart_item"]')
    cart_box = driver.find_element_by_css_selector('#box-checkout-summary')
    ActionChains(driver).move_to_element(remove_buttons[0]).click_and_hold().release().perform()
    wait.until(EC.invisibility_of_element(cart_box))
    assert len(driver.find_elements_by_css_selector('td.item')) == 0
