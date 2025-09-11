import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.buttons_page import ButtonsPage
from pages.links import LinksPage
from pages.download import UploadAndDownloadPage
from pages.dynamic_properties_page import DynamicPropertiesPage
from pages.form_page import FormPage
from pages.browser_window import BrowserWindowPage
from pages.alerts import Alerts
from pages.frames import Frames
from pages.nested_frames import NestedFramesPage
from pages.modal_dialogs import ModalDialogsPage
from pages.resizable import ResizablePage
from pages.selectable import SelectablePage
from pages.sortable import Sortable
from pages.widgests import Widgets
from pages.auto_complete import Auto
from pages.date_picker import DatePicker
from pages.slider import SliderPage
from pages.progres_bar import ProgressBar
from pages.tables import TablesPage
from pages.tool_tips import Tooltips
from pages.menu import MenuPage
from pages.select_menu import SelectMenu



# ---------- FIXTURE ДЛЯ ДРАЙВЕРА ----------
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield driver  # віддаємо драйвер у тест
    driver.quit()  # закриваємо після завершення


# ---------- CONTAINER ДЛЯ СТОРІНОК ----------
class Pages:
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.buttons_page = ButtonsPage(driver)
        self.links_page = LinksPage(driver)
        self.download_page = UploadAndDownloadPage(driver)
        self.dynamic_properties_page = DynamicPropertiesPage(driver)
        self.form_page = FormPage(driver)
        self.browser_window = BrowserWindowPage(driver)
        self.alerts_page = Alerts(driver)
        self.frames_page = Frames(driver)
        self.nested_frames_page = NestedFramesPage(driver)
        self.modal_dialogs_page = ModalDialogsPage(driver)
        self.widgets_page = Widgets(driver)
        self.auto_complete = Auto(driver)
        self.date_picker = DatePicker(driver)
        self.slider = SliderPage(driver)
        self.progress_bar = ProgressBar(driver)
        self.tables = TablesPage(driver)
        self.tooltips = Tooltips(driver)
        self.menu = MenuPage(driver)
        self.select_menu = SelectMenu(driver)
        self.sortable = Sortable(driver)
        self.selectable = SelectablePage(driver)
        self.resizable = ResizablePage(driver)



# ---------- FIXTURE ДЛЯ PAGES ----------
@pytest.fixture
def pages(driver):
    return Pages(driver)
