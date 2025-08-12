import email
import os
import random
from os import path
from selenium.webdriver.remote.webdriver import WebDriver

from pywin.framework.intpyapp import lastLocateFileName
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
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
    SUBJECT = (By.ID, "subjectsInput")
    HOBBIES = (By.CSS_SELECTOR, f"label[for='hobbies-checkbox-{random.randint(1, 3)}']")
    FILE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    SELECT_STATE = (By.ID, "state")
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
       self.wait.until(EC.visibility_of_element_located(self.HOBBIES)).click()
       self.wait.until(EC.visibility_of_element_located(self.SUBJECT)).send_keys('Maths')
       self.wait.until(EC.visibility_of_element_located(self.SUBJECT)).send_keys(Keys.RETURN)
       self.wait.until(EC.presence_of_element_located(self.FILE_INPUT)) \
           .send_keys(r"C:\Users\Sviatko\Desktop\Англійська\зображення_viber_2025-07-24_13-35-51-948.jpg")
       self.wait.until(EC.visibility_of_element_located(self.CURRENT_ADDRESS)).send_keys('Святіко')
       self.wait.until(EC.presence_of_element_located(self.SELECT_STATE)).click()

    # def select_state(self, state_name: str):
    #     # Клік по контейнеру дропдауну
    #     self.wait.until(EC.element_to_be_clickable(self.SELECT_STATE)).click()
    #
    #     # Ввести значення в інпут
    #     self.wait.until(EC.visibility_of_element_located(self.STATE_INPUT)).send_keys("Haryana")
    #
    #     # Підтвердити вибір
    #     self.wait.until(EC.visibility_of_element_located(self.STATE_INPUT)).send_keys(Keys.ENTER)
    #
    #
    #

