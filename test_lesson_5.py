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

    # Check geo zones sorting
    driver.get('http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones')
    geo_zones_page_rows = driver.find_elements_by_css_selector('.row td:nth-child(3) a')
    geo_zones_list = []
    for x in range(len(geo_zones_page_rows)):
        geo_zones_list.append(geo_zones_page_rows[x].get_attribute('textContent'))
    geo_zones_list_sorted = list(geo_zones_list)
    geo_zones_list_sorted.sort()
    for x in range(len(geo_zones_list)):
        assert geo_zones_list[x] == geo_zones_list_sorted[x]


def test_check_product_pages(driver):
    driver.get('http://localhost/litecart/public_html')
    for x in range(len(driver.find_elements_by_class_name('product'))):
        price1 = price2 = price3 = product_price1 = product_price2 = product_price3 = None
        driver.get('http://localhost/litecart/public_html')
        products_list = driver.find_elements_by_class_name('product')
        name = products_list[x].find_element_by_css_selector('.name').get_attribute('textContent')
        sticker = products_list[x].find_element_by_css_selector('.sticker').get_attribute('textContent')
        price = products_list[x].find_elements_by_css_selector('.price')
        if len(price) > 0:
            price1 = price[0].get_attribute('textContent')
        regular_price = products_list[x].find_elements_by_css_selector('.regular-price')
        if len(regular_price) > 0:
            price2 = regular_price[0].get_attribute('textContent')
        campaign_price = products_list[x].find_elements_by_css_selector('.campaign-price')
        if len(campaign_price) > 0:
            price3 = campaign_price[0].get_attribute('textContent')
        img_alt_text = products_list[x].find_element_by_css_selector('img').get_attribute('alt')
        products_list[x].click()
        product_page = driver.find_element_by_css_selector('#box-product')
        product_title = product_page.find_element_by_css_selector('.title').get_attribute('textContent')
        product_sticker = product_page.find_element_by_css_selector('.sticker').get_attribute('textContent')
        product_price = product_page.find_elements_by_css_selector('.price')
        if len(product_price) > 0:
            product_price1 = product_price[0].get_attribute('textContent')
        product_regular_price = product_page.find_elements_by_css_selector('.regular-price')
        if len(product_regular_price) > 0:
            product_price2 = product_regular_price[0].get_attribute('textContent')
        product_campaign_price = product_page.find_elements_by_css_selector('.campaign-price')
        if len(product_campaign_price) > 0:
            product_price3 = product_campaign_price[0].get_attribute('textContent')
        product_img_alt_text = product_page.find_element_by_css_selector('img').get_attribute('alt')

        assert name == product_title
        assert sticker == product_sticker
        assert price1 == product_price1
        assert price2 == product_price2
        assert price3 == product_price3
        assert img_alt_text == product_img_alt_text
