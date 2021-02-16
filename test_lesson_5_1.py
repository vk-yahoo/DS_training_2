# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_admin_sections(driver):
    """
    Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.
    1. на странице http://localhost/litecart/admin/?app=countries&doc=countries
        а) проверить, что страны расположены в алфавитном порядке
        б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить,
        что зоны расположены в алфавитном порядке
    2. на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones зайти в каждую из стран и проверить,
    что зоны расположены в алфавитном порядке
    """
    driver.get("http://localhost/litecart/public_html/admin")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    # Check countries sorting
    driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
    country_page_rows = driver.find_elements_by_css_selector('.row td:nth-child(5) a')
    countries_list = []
    for x in range(len(country_page_rows)):
        countries_list.append(country_page_rows[x].get_attribute('textContent'))
    countries_list_sorted = list(countries_list)
    countries_list_sorted.sort()
    for x in range(len(countries_list)):
        assert countries_list[x] == countries_list_sorted[x]
    print('\ncountries_list')
    print(countries_list)

    # Check zones sorting on country page
    driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
    country_rows = driver.find_elements_by_css_selector('.row')
    for x in range(len(country_rows)):
        if country_rows[x].find_element_by_css_selector('td:nth-child(6)').get_attribute('textContent') != '0':
            country_rows[x].find_element_by_css_selector('td:nth-child(5) a').click()
            zones_names = driver.find_elements_by_css_selector('#table-zones tr td:nth-child(3)')
            zones_list = []
            for zone in range(len(zones_names)-1):
                zones_list.append(zones_names[zone].get_attribute('textContent'))
            zones_list_sorted = list(zones_list)
            zones_list_sorted.sort()
            for y in range(len(zones_names)-1):
                assert zones_list[y] == zones_list_sorted[y]
            print('\nzones_list')
            print(zones_list)
            driver.get('http://localhost/litecart/public_html/admin/?app=countries&doc=countries')
            country_rows = driver.find_elements_by_css_selector('.row')

    # Check geo zones sorting on geo zones page
    driver.get('http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones')
    countries = driver.find_elements_by_css_selector('.row td:nth-child(3) a')
    for country in range(len(countries)):
        countries[country].click()
        zones_list = []
        zones = driver.find_elements_by_css_selector('#table-zones tr td:nth-child(3) select')
        for zone in range(len(zones)):
            select = Select(zones[zone])
            zones_list.append(select.first_selected_option.get_attribute("textContent"))
        zones_list_sorted = list(zones_list)
        zones_list_sorted.sort()
        for x in range(len(zones_list)):
            assert zones_list[x] == zones_list_sorted[x]
        driver.get('http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones')
        countries = driver.find_elements_by_css_selector('.row td:nth-child(3) a')
        print('\nzones_list')
        print(zones_list)
        print(zones_list_sorted)
