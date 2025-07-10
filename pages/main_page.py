from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver


class MainPage:
    sign_in_btn = (By.CSS_SELECTOR, "a.btn.btn-s")
    email_field = (By.CSS_SELECTOR, "#email")
    password_field = (By.CSS_SELECTOR, "#password")
    sign_in = (By.CSS_SELECTOR, "button.btn")
    go_out = (By.CSS_SELECTOR,"button[aria-label='User menu']")
    out_btn = (By.CSS_SELECTOR,"a[title='Выйти']")

    def log_out(self, driver):
       go_out_window = self.wait.until(EC.visibility_of_element_located(self.go_out))
       actions = ActionChains(driver)
       actions.move_to_element(go_out_window).perform()
       self.wait.until(EC.visibility_of_element_located(self.out_btn)).click()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_on_sign_in_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.sign_in_btn)).click()

    def fill_email(self, text):
        self.wait.until(EC.visibility_of_element_located(self.email_field)).send_keys(text)

    def fill_password(self, text):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(text)

    def click_on_sign_in(self):
        self.wait.until(EC.visibility_of_element_located(self.sign_in)).click()


