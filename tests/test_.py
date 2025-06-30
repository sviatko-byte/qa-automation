from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage
from pages.main_page import MainPage


def test_search_and_login(driver):
    base_page = BasePage(driver)
    base_page.open('https://coursehunter.net/')

    main_page = MainPage(driver)
    main_page.click_on_sign_in_btn()
    main_page.fill_email("4ester31029@gmail.com")
    main_page.fill_password("Taras1994!")
    main_page.click_on_sign_in()
    time.sleep(3)

