import os
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


class AdminCatalogPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog')
        return self

    @property
    def add_new_product_button(self):
        return self.driver.find_element_by_xpath("//*[contains(text(), 'Add New Product')]")

    def add_new_product(self, product):
        self.add_new_product_button.click()
        time.sleep(1)
        # Add data on "General" tab
        self.driver.find_element_by_css_selector('[type="radio"][value="1"]').click()
        self.driver.find_element_by_css_selector('[name="name[en]"]').send_keys(product.title)
        self.driver.find_element_by_css_selector('[name="code"]').send_keys(product.code)
        self.driver.find_element_by_css_selector('[data-name="Root"]').click()
        self.driver.find_element_by_css_selector('[data-name="Rubber Ducks"]').click()
        self.driver.find_element_by_css_selector('[name="product_groups[]"][value="1-3"]').click()
        product_quantity = self.driver.find_element_by_css_selector('[name="quantity"]')
        product_quantity.clear()
        product_quantity.send_keys(product.quantity)

        # Add image
        self.driver.find_element_by_css_selector('[name="new_images[]"]').send_keys(os.getcwd() + "/001.jpg")

        self.driver.find_element_by_css_selector('[name="date_valid_from"]').send_keys(22022021)
        self.driver.find_element_by_css_selector('[name="date_valid_to"]').send_keys(31122021)

        # Add data on "Information" tab
        self.driver.find_element_by_css_selector('.index li:nth-child(2)').click()
        time.sleep(1)
        select_manufacturer = Select(self.driver.find_element_by_css_selector('[name="manufacturer_id"]'))
        select_manufacturer.select_by_visible_text("ACME Corp.")
        self.driver.find_element_by_css_selector('[name="keywords"]').send_keys(product.keywords)
        self.driver.find_element_by_css_selector('[name="short_description[en]"]').send_keys(product.short_description)
        self.driver.find_element_by_css_selector('.trumbowyg-editor').send_keys(product.long_description)
        self.driver.find_element_by_css_selector('[name="head_title[en]"]').send_keys(product.head_title)
        self.driver.find_element_by_css_selector('[name="meta_description[en]"]').send_keys(product.meta_description)

        # Add data on "Information" tab
        self.driver.find_element_by_css_selector('.index li:nth-child(4)').click()
        time.sleep(1)

        purchase_price = self.driver.find_element_by_css_selector('[name="purchase_price"]')
        purchase_price.clear()
        purchase_price.send_keys(product.purchase_price)
        select_currency = Select(self.driver.find_element_by_css_selector('[name="purchase_price_currency_code"]'))
        select_currency.select_by_visible_text("Euros")

        self.driver.find_element_by_css_selector('[name="save"]').click()
        time.sleep(1)

    def assert_product_adding(self, product):
        # Variant 1
        catalog = self.driver.find_element_by_css_selector('[name="catalog_form"]')
        catalog.find_elements_by_xpath('//a[contains(text(), "%s")]' % product.title)

        # Variant 2
        assert product.title in self.driver.find_element_by_css_selector(
            '[name="catalog_form"]').get_attribute("textContent")

        # Variant 3
        elements = self.driver.find_elements_by_css_selector('[name="catalog_form"] a')
        for element in elements:
            if element.get_attribute("textContent") == product.title:
                print(element)
        return True
