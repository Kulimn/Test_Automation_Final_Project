from selenium.webdriver.common.by import By

amount = (By.XPATH, "//*[@id='tvAmount']")
term = (By.XPATH, "//*[@id='tvTerm']")
rate = (By.XPATH, "//*[@id='tvRate']")
delete = (By.XPATH, "//*[@id='btnDel']")
confirm_delete = (By.XPATH, "//*[@text='OK']")


class SavedPage:
    def __init__(self, driver):
        self.driver = driver

    def get_amount(self):
        return self.driver.find_element(amount[0], amount[1])

    def get_term(self):
        return self.driver.find_element(term[0], term[1])

    def get_rate(self):
        return self.driver.find_element(rate[0], rate[1])

    def get_delete(self):
        return self.driver.find_element(delete[0], delete[1])

    def get_confirm_delete(self):
        return self.driver.find_element(confirm_delete[0], confirm_delete[1])