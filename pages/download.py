from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.conftest import driver

class UploadAndDownloadPage:
    download_btn = (By.ID, "downloadButton")
    upload_locators = (By.ID,"uploadFile")
    text_locators = (By.ID,"uploadedFilePath")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_on_download_btn(self):
        self.wait.until(EC.visibility_of_element_located(self.download_btn)).click()

    def upload_file(self, path):
        self.wait.until(EC.visibility_of_element_located(self.upload_locators)).send_keys(path)

    def should_be_visible_success_upload_message(self):
        self.wait.until(EC.visibility_of_element_located(self.text_locators))
