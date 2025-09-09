import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FormPage():

    def __init__(self, driver: WebDriver):
        self.wait = WebDriverWait(driver, 5)
        self.driver = driver

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    #GENDER = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE = (By.ID, "userNumber")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "dateOfBirthInput")
    SUBJECT = (By.ID, "subjectsInput")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    SELECT_STATE = (By.ID, "state")
    STATE_INPUT = (By.ID, "react-select-3-input")
    SELECT_CITY = (By.ID, "city")
    CITY_INPUT = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")

    def fill_form_fields(self, name, last_name, email, mobile):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(name)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        self.wait.until(EC.visibility_of_element_located(self.MOBILE)).send_keys(mobile)
        element = self.wait.until(EC.visibility_of_element_located(self.CURRENT_ADDRESS))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.wait.until(EC.visibility_of_element_located(self.GENDER)).click()
        self.wait.until(EC.visibility_of_element_located(self.HOBBIES)).click()
        self.wait.until(EC.visibility_of_element_located(self.SUBJECT)).send_keys('Maths')
        self.wait.until(EC.visibility_of_element_located(self.SUBJECT)).send_keys(Keys.RETURN)
        self.wait.until(EC.presence_of_element_located(self.FILE_INPUT)).send_keys(
            r"C:\Users\dewif\OneDrive\Робочий стіл\Англійська\зображення_viber_2025-08-16_13-21-12-947.jpg"
        )
        self.wait.until(EC.visibility_of_element_located(self.CURRENT_ADDRESS)).send_keys('Святіко')

    def select_state(self, state_name: str):
        state_container = self.wait.until(EC.element_to_be_clickable(self.SELECT_STATE))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_container)
        state_container.click()
        state_input = self.wait.until(EC.visibility_of_element_located(self.STATE_INPUT))
        state_input.send_keys(state_name)
        state_input.send_keys(Keys.ENTER)

    def select_city(self, state_name: str):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_CITY)).click()
        self.wait.until(EC.visibility_of_element_located(self.CITY_INPUT)).send_keys(state_name)
        self.wait.until(EC.visibility_of_element_located(self.CITY_INPUT)).send_keys(Keys.ENTER)

    def click_on_submit_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT)).click()






