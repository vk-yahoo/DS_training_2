from selenium.webdriver.support.wait import WebDriverWait


class AppMainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/public_html")
        return self

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
