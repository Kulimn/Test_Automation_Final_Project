from selenium.webdriver.common.by import By

btn_back_to_products = (By.ID, 'back-to-products')


class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_back_to_products(self):
        return self.driver.find_elements(btn_back_to_products[0], btn_back_to_products[1])
