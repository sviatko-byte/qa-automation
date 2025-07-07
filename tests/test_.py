import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from pages.base_page import BasePage
from pages.buttons_page import ButtonsPage
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
    main_page.log_out(driver)




def test_different_click_on_the_buttons(driver):
    base_page = BasePage(driver)
    base_page.open('https://demoqa.com/buttons')
""
    buttons_page = ButtonsPage(driver)
    # Виконуємо подвійний клік
    buttons_page.double_click()
    buttons_page.should_display_double_click_message('You have done a double click')
    buttons_page.right_click()
    buttons_page.should_display_right_click_message('You have done a right click')



