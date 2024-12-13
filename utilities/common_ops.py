import csv
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET

def get_data(node_name):
    root = ET.parse('/Users/sergeykiseliov/Desktop/test_automation_finel_project1/configurations/data.xml').getroot()
    return root.find('.//' + node_name).text

def wait(for_element, elem):
    if for_element == 'element_exists':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.presence_of_element_located((elem[0], elem[1])))
    elif for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data('WaitTime'))).until(EC.visibility_of_element_located((elem[0], elem[1])))

def read_csv(file_name):
    data = []
    with open(file_name, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            data.insert(len(data), row)
        return data

def get_time_stamp():
    return time.time()

#Enum for selecting displayed element or exist element, my wait method uses this enum
class For:
    ELEMENT_EXISTS = 'element_exists'
    ELEMENT_DISPLAYED = 'element_displayed'

#Enum for selecting product for delete
class By:
    PRODUCT = 'product'
    INDEX = 'index'

class Product_Type:
    BACKPACK = 'remove-sauce-labs-backpack'
    BIKE_LIGHT = 'remove-sauce-labs-bike-light'
    BOLT_T_SHIRT = 'remove-sauce-labs-bolt-t-shirt'
    FLEECE_JACKET = 'remove-sauce-labs-fleece-jacket'
    ONESIE = 'remove-sauce-labs-onesie'
    T_SHIRT_RED = 'remove-test.allthethings()-t-shirt-(red)'

# Enum for selecting whether we want to save mortgage transaction or not
class Save:
    YES = True
    NO = False

# Enum for selecting swip direction
class Direction:
    LEFT = 'left'
    RIGHT = 'right'
    UP = 'up'
    DOWN = 'down'

