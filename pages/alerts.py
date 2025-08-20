import time

from selenium.webdriver.common.by import By




class Alerts:
    def __init__(self, driver):
        self.driver = driver


    SEE_ALERT_BUTTON = 'alertButton'
    APPEAR_ALERT_5SEC_BUTTON = 'timerAlertButton'
    CONFIRM_BOX = 'confirmButton'
    PROMPT_BOX = 'promtButton'


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
