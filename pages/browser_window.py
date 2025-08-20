

import selenium
from selenium.webdriver.common.by import By


class BrowserWindowPage:
    def __init__(self, driver):
        self.driver = driver

    NEW_TAB_BUTTON = 'tabButton'
    TITLE = 'sampleHeading'
    WINDOW_BUTTON = 'windowButton'
    WINDOW_TITLE = 'sampleHeading'



    def click_on_submit_btn(self):
        self.driver.find_element(By.ID, self.NEW_TAB_BUTTON).click()

    def switch_to_window(self, value):
        self.driver.switch_to.window(self.driver.window_handles[value])

    def get_page_title(self):
        text_title = self.driver.find_element(By.ID, self.TITLE).text
        print(text_title)

    def click_on_new_window_btn(self):
        self.driver.find_element(By.ID, self.WINDOW_BUTTON).click()

    def get_on_new_window_title(self):
        text_on_title = self.driver.find_element(By.ID, self.WINDOW_TITLE).text
        print(text_on_title)