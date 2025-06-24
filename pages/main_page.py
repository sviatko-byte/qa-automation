from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    search_field_locator = (By.CSS_SELECTOR, "input[placeholder='Я шукаю...']")
    search_btn_locator = (By.XPATH, "//button[contains(text(),'Знайти')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def fill_search_field(self, text):
        field = self.wait.until(EC.visibility_of_element_located(self.search_field_locator))
        field.clear()
        field.send_keys(text)

    def click_search_button(self):
        button = self.wait.until(EC.element_to_be_clickable(self.search_btn_locator))
        button.click()
