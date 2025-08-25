import os
from selenium import webdriver
import time
from data.constans import DefaultConstants, Urls
from pages.alerts import Alerts
from pages.base_page import BasePage
from pages.browser_window import  BrowserWindowPage
from pages.buttons_page import ButtonsPage
from pages.download import UploadAndDownloadPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.form_page import FormPage
from pages.links import LinksPage
from pages.main_page import MainPage
from pages.modal_dialogs import ModalDialogsPage
from pages.nested_frames import NestedFramesPage
from pages.widgests import Widgets
from utils.helpers import is_file_downloaded, create_random_file, generate_random_name, generate_random_email, generate_random_mobile
from pages.frames import Frames


driver = webdriver.Chrome()

base_page = BasePage(driver)
main_page = MainPage(driver)
buttons_page = ButtonsPage(driver)
links_page = LinksPage(driver)
download_page = UploadAndDownloadPage(driver)
dynamic_properties_page = DynamicPropertiesPage(driver)
form_page = FormPage(driver)
browser_window = BrowserWindowPage(driver)
alerts_page = Alerts(driver)
frames_page = Frames(driver)
nested_frames_page = NestedFramesPage(driver)
modal_dialogs_page = ModalDialogsPage(driver)
widgets_page = Widgets(driver)

def test_search_and_login():
    base_page.open(Urls.COURSEHUNTER)
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
    base_page.open(Urls.LINKS)
    links_page.check_new_tab_simple_link()


def test_broken_link():
    base_page.open(Urls.LINKS)
    links_page.check_broken_link()

def test_download():
    base_page.open(Urls.DOWNLOAD)
    download_page.click_on_download_btn()
    full_path = os.path.join(DefaultConstants.download_dir, DefaultConstants.filename)
    assert is_file_downloaded(full_path), "❌ Файл не знайдено або не скачався!"


def test_upload():
    base_page.open(Urls.UPLOAD)
    path = create_random_file(DefaultConstants.download_dir)
    download_page.upload_file(path)
    download_page.should_be_visible_success_upload_message()

def test_dynamic_properties_page():
    base_page.open(Urls.DYNAMIC_PROPERTIES)
    dynamic_properties_page.check_changed_color()



def test_form():
    base_page.open(Urls.FORM)
    random_name = generate_random_name(length=6)
    random_email = generate_random_email( length=8)
    random_mobile = generate_random_mobile()

    form_page.fill_form_fields(name=random_name, last_name=random_name, email=random_email, mobile=random_mobile)
    form_page.select_state('NCR')
    form_page.select_city('Noida')
    form_page.click_on_submit_btn()


def test_browser_window():
    base_page.open(Urls.BROWSER_WINDOW)
    browser_window.click_on_submit_btn()
    browser_window.switch_to_window(1)
    browser_window.get_page_title()
    browser_window.switch_to_window(0)
    browser_window.click_on_new_window_btn()
    browser_window.switch_to_window(1)
    browser_window.get_on_new_window_title()


def test_alerts_page():
    base_page.open(Urls.ALERTS)
    alerts_text = alerts_page.check_see_alert()
    alerts_page.accept_alert()
    assert alerts_text == 'You clicked a button'
    alerts_text = alerts_page.check_alert_appear_5_sec()
    assert alerts_text == 'This alert appeared after 5 seconds'
    alerts_page.accept_alert()
    text_result = alerts_page.check_confirm_box()
    assert text_result == 'You selected Ok'
    text_result = alerts_page.check_prompt_box()
    assert text_result

def test_frames_page():
    base_page.open(Urls.FRAMES)
    result_frame1 = frames_page.check_frames("frame1 ")
    result_frame2 = frames_page.check_frames("frame2 ")
    print(result_frame1, result_frame2)

def test_nested_frames_page():
    base_page.open(Urls.NESTED_FRAMES)
    parent_text , child_text = nested_frames_page.check_nested_frames_page()
    print(parent_text, child_text)

def test_modal_dialogs_page():
    base_page.open(Urls.MODAL_DIALOGS)
    small , large = modal_dialogs_page.small_modal_modal()
    print(small)
    print(large)

def test_widgets_page():
    base_page.open(Urls.WIDGETS)
    widgets_page.check_accordian(accordian_num='first')
    widgets_page.check_accordian(accordian_num='second')
    widgets_page.check_accordian(accordian_num='third')
