from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SearchResultPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

        # Локатори (приклади, заміни на реальні з HTML)
        self.add_to_cart_btn = (By.ID, "//a[@href='expected_conditions.html']")
        self.cart_btn = (By.ID, "//a[@href='expected_conditions.html']")
        self.cart_window = (By.ID, "//a[@href='expected_conditions.html']")
        self.link_to_conditions = (By.XPATH, "//a[@href='expected_conditions.html']")

    def click_link_to_conditions(self):
        button = self.wait.until(EC.element_to_be_clickable(self.link_to_conditions))
        button.click()

    def click_add_to_cart_btn(self):
        button = self.wait.until(EC.element_to_be_clickable(self.add_to_cart_btn))
        button.click()

    def click_on_cart_btn(self):
        button = self.wait.until(EC.element_to_be_clickable(self.cart_btn))
        button.click()

    def should_display_cart_window(self):
        window = self.wait.until(EC.visibility_of_element_located(self.cart_window))
        return window.is_displayed()