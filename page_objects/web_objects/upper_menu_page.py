from selenium.webdriver.common.by import By

btn_menu = (By.CLASS_NAME, 'bm-burger-button')
btn_all_items = (By.ID, 'inventory_sidebar_link')
btn_about = (By.ID, 'about_sidebar_link')
btn_logout = (By.ID, 'logout_sidebar_link')
btn_reset_app_state = (By.ID, 'reset_sidebar_link')
product_sort = (By.CLASS_NAME, 'product_sort_container')
shopping_cart = (By.CLASS_NAME, 'shopping_cart_link')


class UpperMenuPage:
    def __init__(self, driver):
        self.driver = driver

    def get_btn_menu(self):
        return self.driver.find_element(btn_menu[0], btn_menu[1])

    def get_btn_all_items(self):
        return self.driver.find_element(btn_all_items[0], btn_all_items[1])

    def get_btn_about(self):
        self.driver.find_element(btn_about[0], btn_about[1])

    def get_btn_logout(self):
        self.driver.find_element(btn_logout[0], btn_logout[1])

    def get_btn_reset_app_state(self):
        self.driver.find_element(btn_reset_app_state[0], btn_reset_app_state[1])

    def get_product_sort(self):
        return self.driver.find_element(product_sort[0], product_sort[1])

    def get_shopping_cart(self):
        return self.driver.find_element(shopping_cart[0], shopping_cart[1])
