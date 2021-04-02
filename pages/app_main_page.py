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
