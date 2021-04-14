import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class AppMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/public_html")
        time.sleep(1)
        return self

    def login(self, email, password):
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.driver.find_element_by_css_selector('[name="login"]').click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element_by_link_text('Logout').click()
        time.sleep(2)

    @property
    def products(self):
        return self.driver.find_elements_by_class_name('product')

    @property
    def product_stickers(self):
        return self.driver.find_elements_by_css_selector('.product .sticker')

    def get_product_by_index(self, index):
        return self.products[index]

    def stickers_count(self, product_index):
        return len(self.get_product_by_index(product_index).find_elements_by_css_selector('.sticker'))

    def get_campaigns_product_details_hp(self):
        details = {
            "title": self.driver.find_element_by_css_selector('#box-campaigns .product .name').get_attribute(
                'textContent'),
            "sticker": self.driver.find_element_by_css_selector('#box-campaigns .product .sticker').get_attribute(
                'textContent'),
            "price": self.driver.find_element_by_css_selector('#box-campaigns .product .regular-price').get_attribute(
                'textContent'),
            "price color": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .regular-price').value_of_css_property('color'),
            "price text-decoration": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .regular-price').value_of_css_property('text-decoration'),
            "price font-weight": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .regular-price').value_of_css_property('font-weight'),
            "campaign-price": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .campaign-price').get_attribute('textContent'),
            "campaign-price color": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .campaign-price').value_of_css_property('color'),
            "campaign-price font-weight": self.driver.find_element_by_css_selector(
                '#box-campaigns .product .campaign-price').value_of_css_property('font-weight')}
        return details

    def open_product(self):
        self.driver.find_element_by_css_selector('#box-campaigns .product a.link').click()

    def get_campaigns_product_details_pp(self):
        details = {
            "title": self.driver.find_element_by_css_selector('#box-product .title').get_attribute('textContent'),
            "sticker": self.driver.find_element_by_css_selector('#box-product .sticker').get_attribute('textContent'),
            "price": self.driver.find_element_by_css_selector('#box-product .regular-price').get_attribute(
                'textContent'),
            "price color": self.driver.find_element_by_css_selector(
                '#box-product .regular-price').value_of_css_property('color'),
            "price text-decoration": self.driver.find_element_by_css_selector(
                '#box-product .regular-price').value_of_css_property('text-decoration'),
            "price font-weight": self.driver.find_element_by_css_selector(
                '#box-product .regular-price').value_of_css_property('font-weight'),
            "campaign-price": self.driver.find_element_by_css_selector(
                '#box-product .campaign-price').get_attribute('textContent'),
            "campaign-price color": self.driver.find_element_by_css_selector(
                '#box-product .campaign-price').value_of_css_property('color'),
            "campaign-price font-weight": self.driver.find_element_by_css_selector(
                '#box-product .campaign-price').value_of_css_property('font-weight')}
        return details

    def add_user_link_click(self):
        self.driver.find_element_by_css_selector('#box-account-login a').click()
        time.sleep(2)

    @property
    def first_name_input(self):
        return self.driver.find_element_by_css_selector('[name="firstname"]')

    @property
    def last_name_input(self):
        return self.driver.find_element_by_css_selector('[name="lastname"]')

    @property
    def address_input(self):
        return self.driver.find_element_by_css_selector('[name="address1"]')

    @property
    def postcode_input(self):
        return self.driver.find_element_by_css_selector('[name="postcode"]')

    @property
    def city_input(self):
        return self.driver.find_element_by_css_selector('[name="city"]')

    @property
    def country_input(self):
        return self.driver.find_element_by_css_selector('select.select2-hidden-accessible')

    @property
    def email_input(self):
        return self.driver.find_element_by_css_selector('[name="email"]')

    @property
    def phone_input(self):
        return self.driver.find_element_by_css_selector('[name="phone"]')

    @property
    def password_input(self):
        return self.driver.find_element_by_css_selector('[name="password"]')

    @property
    def confirm_password_input(self):
        return self.driver.find_element_by_css_selector('[name="confirmed_password"]')

    @property
    def first_product(self):
        return self.driver.find_elements_by_css_selector('.product')[0]

    @property
    def add_to_the_cart_button(self):
        return self.driver.find_element_by_css_selector('[name="add_cart_product"]')

    @property
    def product_size(self):
        return self.driver.find_elements_by_css_selector('[name="options[Size]"]')

    @property
    def cart_products_number(self):
        return self.driver.find_element_by_css_selector('#cart .quantity')

    @property
    def remove_button(self):
        return self.driver.find_elements_by_css_selector('button[name="remove_cart_item"]')

    @property
    def cart_summary_items(self):
        return self.driver.find_elements_by_css_selector('#box-checkout-summary td.item')

    @property
    def item_mini_views(self):
        return self.driver.find_elements_by_css_selector('a.act')

    def create_account_button_click(self):
        self.driver.find_element_by_css_selector('[name="create_account"]').click()
        time.sleep(2)

    def add_products_to_the_cart(self, count):
        for i in range(1, count+1):
            self.first_product.click()
            if len(self.product_size) == 1:
                select_size = Select(self.product_size[0])
                select_size.select_by_index(1)
            self.add_to_the_cart_button.submit()
            self.wait.until(EC.text_to_be_present_in_element((By.ID, 'cart'), '%s item(s)' % i))
            self.open()

    def remove_products_from_the_cart(self):
        self.cart_products_number.click()
        time.sleep(1)
        cart_box = self.cart_summary_items
        while len(cart_box) > 1:
            ActionChains(self.driver).move_to_element(self.item_mini_views[0]).click_and_hold().release().perform()
            ActionChains(self.driver).move_to_element(self.remove_button[0]).click_and_hold().release().perform()
            self.wait.until(EC.invisibility_of_element(cart_box[0]))
            cart_box = self.cart_summary_items
        ActionChains(self.driver).move_to_element(self.remove_button[0]).click_and_hold().release().perform()
        self.wait.until(EC.invisibility_of_element(cart_box[0]))

    def get_cart_products_number(self):
        return self.cart_products_number.get_attribute('textContent')
