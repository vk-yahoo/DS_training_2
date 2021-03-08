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
    Сделайте сценарий, который проверяет, что ссылки на странице редактирования страны открываются в новом окне.

    Сценарий должен состоять из следующих частей:
    1) зайти в админку
    2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
    3) открыть на редактирование какую-нибудь страну или начать создание новой
    4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой.
    Они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.

    Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank".
    Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне,
    потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.

    Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.
    """
    # Login to the admin
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    # Open Countries page and click on "Add New Country" button
    driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
    driver.find_element_by_css_selector('a.button').click()
    main_window = driver.current_window_handle
    internal_links = driver.find_elements_by_css_selector('#content .fa-external-link')

    # Check external links
    for link in range(len(internal_links)):
        internal_links[link].click()
        available_windows = driver.window_handles
        if available_windows[0] == main_window:
            driver.switch_to.window(available_windows[1])
        else:
            driver.switch_to.window(available_windows[0])
        driver.close()
        driver.switch_to.window(main_window)

    print('\n ')
    print('All %s external links were opened in new window' % len(internal_links))
