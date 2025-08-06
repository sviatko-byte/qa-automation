import email
import random

from pywin.framework.intpyapp import lastLocateFileName
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver


class FormPage():

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    FIRST_NAME = (By.CSS_SELECTOR, "input[id='firstName']")
    LAST_NAME = (By.CSS_SELECTOR, "input[id='lastName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    GENDER = (By.CSS_SELECTOR, f"div[class*='custom-control'] input[id='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, "userNumber")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "dateOfBirthInput")
    SUBJECT = (By.CSS_SELECTOR, "subjectsInput")
    HOBBIES = (By.CSS_SELECTOR, f"//input[@id='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.CSS_SELECTOR, "uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "currentAddress")
    SELECT_STATE = (By.CSS_SELECTOR, "state")
    STATE_INPUT = (By.CSS_SELECTOR, "react-select-3-input")
    SELECT_CITY = (By.CSS_SELECTOR, "city")
    CITY_INPUT = (By.CSS_SELECTOR, "react-select-4-input")
    SUBMIT = (By.CSS_SELECTOR, "submit")




    def fill_form_fields(self, name, last_name, ):
       self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(name)
       self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)

    def fill_random_email(self,email):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)

    def fill_random_numbers(self,mobile):
        self.wait.until(EC.visibility_of_element_located(self.MOBILE)).send_keys(mobile)

