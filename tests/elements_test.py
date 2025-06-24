import time

from pages.base_page import BasePage
from pages.main_page import MainPage


def test(driver):
    base_page = BasePage(driver, 'https://rozetka.com.ua')
    base_page.open()

    main_page = MainPage(driver)
    main_page.fill_search_field(text="Iphone")
    main_page.click_search_button()