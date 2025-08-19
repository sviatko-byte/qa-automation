import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage

class DynamicPropertiesPage:


    COLOR_CHANGE_BUTTON = (By.ID, "colorChange")
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.ID, "visibleAfter")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("check_changed_color")
    def check_changed_color(self):
        self.wait.until(EC.visibility_of_element_located(self.COLOR_CHANGE_BUTTON)).click()
