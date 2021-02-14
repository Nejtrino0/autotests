from webium import Find, Finds
from selenium.webdriver.common.by import By


class NPMPageLocators:
    search_input = Find(by=By.CSS_SELECTOR, value='input[type=search]')
    search_button = Find(by=By.CSS_SELECTOR, value='button[type=submit]')
    result_list = Finds(by=By.CSS_SELECTOR, value='h3.no-underline.hover-black')
