# -*- coding: utf-8 -*-
import time
import datetime

import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_app_add_user(driver):
    """
    Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (в клиентской части магазина).
    Сценарий должен состоять из следующих частей:
    1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты
    2) выход (logout), потому что после успешной регистрации автоматически происходит вход
    3) повторный вход в только что созданную учётную запись
    4) и ещё раз выход.

    В качестве страны выбирайте United States, штат произвольный. При этом формат индекса - пять цифр.
    Проверки можно никакие не делать, только действия - заполнение полей, нажатия на кнопки и ссылки.
    Критерий успеха: сценарий дошёл до конца, созданный пользователь смог выполнить вход и выход.
    В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.
    """
    rand = str(datetime.datetime.now().strftime("%f"))
    first_name = 'Test_' + rand
    last_name = 'User_' + rand
    email = 'litecart' + rand + '@mailinator.com'
    driver.get('http://localhost/litecart/public_html')
    # Click new customers link
    driver.find_element_by_css_selector('#box-account-login a').click()
    time.sleep(2)

    # Input first name
    driver.find_element_by_css_selector('[name="firstname"]').send_keys(first_name)
    # Input last name
    driver.find_element_by_css_selector('[name="lastname"]').send_keys(last_name)
    # Input address
    driver.find_element_by_css_selector('[name="address1"]').send_keys('Some address')
    # Input postcode
    driver.find_element_by_css_selector('[name="postcode"]').send_keys('12345')
    # Input city
    driver.find_element_by_css_selector('[name="city"]').send_keys('Babylon')
    # Select country
    driver.find_element_by_css_selector('select.select2-hidden-accessible').send_keys('United States')
    # Input email
    driver.find_element_by_css_selector('[name="email"]').send_keys(email)
    # Input phone
    driver.find_element_by_css_selector('[name="phone"]').send_keys('911')
    # Input password
    driver.find_element_by_css_selector('[name="password"]').send_keys('123qweASD')
    # Confirm password
    driver.find_element_by_css_selector('[name="confirmed_password"]').send_keys('123qweASD')
    # Click "Create account" button
    driver.find_element_by_css_selector('[name="create_account"]').click()
    time.sleep(2)

    # Logout
    driver.find_element_by_link_text('Logout').click()
    time.sleep(2)

    # Login
    driver.find_element_by_css_selector('[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('[name="password"]').send_keys('123qweASD')
    driver.find_element_by_css_selector('[name="login"]').click()
    time.sleep(2)

    # Logout
    driver.find_element_by_link_text('Logout').click()
    time.sleep(2)
