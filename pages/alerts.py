import random
import time

from selenium.webdriver.common.by import By


class Alerts:
    def __init__(self, driver):
        self.driver = driver


    SEE_ALERT_BUTTON = 'alertButton'
    APPEAR_ALERT_5SEC_BUTTON = 'timerAlertButton'
    CONFIRM_BOX = 'confirmButton'
    CONFIRM_RESULT = 'confirmResult'
    PROMPT_BOX = 'promtButton'
    PROMPT_RESULT = 'promptResult'

    def check_see_alert(self):
        self.driver.find_element(By.ID, self.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        return alert_window.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def check_alert_appear_5_sec(self):
        self.driver.find_element(By.ID, self.APPEAR_ALERT_5SEC_BUTTON).click()
        time.sleep(7)
        alert_window = self.driver.switch_to.alert
        print(alert_window.text)
        return alert_window.text

    def check_confirm_box(self):
        self.driver.find_element(By.ID, self.CONFIRM_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.driver.find_element(By.ID, self.CONFIRM_RESULT).text
        return text_result

    def check_prompt_box(self):
        text = f"autotest{random.randint(0,999)}"
        self.driver.find_element(By.ID, self.PROMPT_BOX).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.driver.find_element(By.ID, self.CONFIRM_RESULT).text
        return text,text_result


