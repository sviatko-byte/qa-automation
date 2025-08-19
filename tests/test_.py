import os
from random import random

from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from data.constans import DefaultConstants
from pages.base_page import BasePage
from pages.browser_window import  BrowserWindowPage
from pages.buttons_page import ButtonsPage
from pages.download import UploadAndDownloadPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.form_page import FormPage
from pages.links import LinksPage
from pages.main_page import MainPage
from utils.helpers import is_file_downloaded, create_random_file, generate_random_name, generate_random_email, \
    generate_random_numbers, generate_random_mobile

driver = webdriver.Chrome()

base_page = BasePage(driver)
main_page = MainPage(driver)
buttons_page = ButtonsPage(driver)
links_page = LinksPage(driver)
download_page = UploadAndDownloadPage(driver)
dynamic_properties_page = DynamicPropertiesPage(driver)
formpage = FormPage(driver)
browser_window = BrowserWindowPage(driver)


def test_search_and_login():
    base_page.open('https://coursehunter.net/')
    main_page.click_on_sign_in_btn()
    main_page.fill_email(DefaultConstants.login)
    main_page.fill_password(DefaultConstants.password)
    main_page.click_on_sign_in()
    time.sleep(3)
    main_page.log_out(driver)




def test_different_click_on_the_buttons():
    base_page.open('https://demoqa.com/buttons')
    buttons_page.double_click()
    buttons_page.should_display_double_click_message('You have done a double click')
    buttons_page.right_click()
    buttons_page.should_display_right_click_message('You have done a right click')


def test_check_link():
    base_page.open('https://demoqa.com/links')
    links_page.check_new_tab_simple_link()


def test_broken_link():
    base_page.open('https://demoqa.com/links')
    links_page.check_broken_link()

def test_download():
    base_page.open('https://demoqa.com/upload-download')
    download_page.click_on_download_btn()
    full_path = os.path.join(DefaultConstants.download_dir, DefaultConstants.filename)
    assert is_file_downloaded(full_path), "❌ Файл не знайдено або не скачався!"


def test_upload():
    base_page.open('https://demoqa.com/upload-download')
    path = create_random_file(DefaultConstants.download_dir)
    download_page.upload_file(path)
    download_page.should_be_visible_success_upload_message()

def test_dynamic_properties_page():
    base_page.open('https://demoqa.com/dynamic-properties')
    dynamic_properties_page.check_changed_color()



def test_form():
    base_page.open('https://demoqa.com/automation-practice-form')
    random_name = generate_random_name(length=6)
    random_email = generate_random_email( length=8)
    random_mobile = generate_random_mobile()

    formpage.fill_form_fields(name=random_name, last_name=random_name, email=random_email, mobile=random_mobile)
    formpage.select_state('NCR')
    formpage.select_city('Noida')
    formpage.click_on_submit_btn()

    driver.quit()


def test_browser_window():
    base_page.open('https://demoqa.com/browser-windows')
    browser_window.click_on_submit_btn()
    browser_window.switch_to_window(1)
    browser_window.get_page_title()
    browser_window.switch_to_window(0)
    browser_window.click_on_new_window_btn()
    driver.quit()








