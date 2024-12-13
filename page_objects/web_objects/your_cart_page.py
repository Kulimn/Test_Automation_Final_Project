from selenium.webdriver.common.by import By

products_list = (By.CLASS_NAME, 'inventory_item_name')
delete_product = (By.ID, 'remove')
shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')
delete_by_product_name = (By.XPATH, '//*[@id="kuku"]')
btn_continue_shopping = (By.ID, 'continue-shopping')
btn_checkout = (By.ID, 'checkout')


class YourCartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_products_list(self):
        return self.driver.find_elements(products_list[0], products_list[1])

    def get_products_by_index(self, index):
        return self.get_products_list()[index]

    def get_delete_product(self):
        return self.driver.find_element(delete_product[0], delete_product[1])

    def get_shopping_cart(self):
        return self.driver.find_element(shopping_cart[0], shopping_cart[1])

    def get_delete_by_product_name(self, product):
        return self.driver.find_element(delete_by_product_name[0], delete_by_product_name[1].replace('kuku', str(product)))

    def get_btn_continue_shopping(self):
        return self.driver.find_elements(btn_continue_shopping[0], btn_continue_shopping[1])

    def get_btn_checkout(self):
        return self.driver.find_element(btn_checkout[0], btn_checkout[1])
