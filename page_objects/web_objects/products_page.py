from selenium.webdriver.common.by import By

btn_atc_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
btn_atc_black_shirt = (By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt')
btn_atc_onesie = (By.ID, 'add-to-cart-sauce-labs-onesie')
btn_atc_bike = (By.ID, 'add-to-cart-sauce-labs-bike-light')
btn_atc_jacket = (By.ID, 'add-to-cart-sauce-labs-fleece-jacket')
btn_atc_red_shirt = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')


class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_atc_backpack(self):
        return self.driver.find_element(btn_atc_backpack[0], btn_atc_backpack[1])

    def get_btn_atc_black_shirt(self):
        return self.driver.find_element(btn_atc_black_shirt[0], btn_atc_black_shirt[1])

    def get_btn_atc_onesie(self):
        return self.driver.find_element(btn_atc_onesie[0], btn_atc_onesie[1])

    def get_btn_atc_bike(self):
        return self.driver.find_element(btn_atc_bike[0], btn_atc_bike[1])

    def get_btn_atc_jacket(self):
        return self.driver.find_element(btn_atc_jacket[0], btn_atc_jacket[1])

    def get_btn_atc_red_shirt(self):
        return self.driver.find_element(btn_atc_red_shirt[0], btn_atc_red_shirt[1])
