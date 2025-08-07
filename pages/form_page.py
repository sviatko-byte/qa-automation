import email
import random

from pywin.framework.intpyapp import lastLocateFileName
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class FormPage():

    def __init__(self, driver: WebDriver):
        self.wait = WebDriverWait(driver, 5)

    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    #GENDER = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE = (By.ID, "userNumber")
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




    def fill_form_fields(self, name, last_name, email, mobile):
       self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(name)
       self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last_name)
       self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
       self.wait.until(EC.visibility_of_element_located(self.MOBILE)).send_keys(mobile)
       self.wait.until(EC.visibility_of_element_located(self.GENDER)).click()


