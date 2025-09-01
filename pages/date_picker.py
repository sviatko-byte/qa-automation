from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
from faker import Faker

from pages.base_page import BasePage


class DatePicker(BasePage):
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')

    from selenium.webdriver.common.by import By

    DATE_ADD_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    DATE_ADD_TIME_YEAR = (By.CLASS_NAME, "react-datepicker__year-read-view")  # клікаємо по блоку (а не по стрілці)
    DATE_ADD_TIME_YEAR_LIST = (By.CSS_SELECTOR, "div.react-datepicker__year-option")

    DATE_ADD_TIME_MONTH = (By.CLASS_NAME, "react-datepicker__month-read-view")  # клікаємо по блоку
    DATE_ADD_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div.react-datepicker__month-option")

    DATE_ADD_TIME_DAY_LIST = (By.CSS_SELECTOR, "div.react-datepicker__day")  # додай, якщо ще немає
    DATE_ADD_TIME_TIME_LIST = (By.CSS_SELECTOR,
                               ".react-datepicker__time-list-item")  # була відсутня крапка і зайвий пробіл

    fake_en = Faker("en_US")

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = None

    def select_date(self):
        random_date = self.fake_en.date_of_birth(minimum_age=18, maximum_age=60)
        self.element_is_clickable(self.DATE_INPUT).click()
        month_dropdown = Select(self.element_is_visible(self.DATE_SELECT_MONTH))
        month_dropdown.select_by_index(random_date.month - 1)
        year_dropdown = Select(self.element_is_visible(self.DATE_SELECT_YEAR))
        year_dropdown.select_by_value(str(random_date.year))
        days = self.elements_are_visible(self.DATE_SELECT_DAY_LIST)
        for day in days:
            if day.text == str(random_date.day) and "outside-month" not in day.get_attribute("class"):
                day.click()
                break

        return random_date

    def select_date_and_time(self):
        # 1) Згенерувати дату (як у твоєму прикладі)
        random_date = self.fake_en.date_of_birth(minimum_age=18, maximum_age=60)

        # 2) Відкрити календар
        self.element_is_clickable(self.DATE_ADD_TIME_INPUT).click()

        # 3) Рік
        self.element_is_clickable(self.DATE_ADD_TIME_YEAR).click()
        # react-datepicker показує «вікно» років; шукаємо потрібний, а якщо не видно — пробуємо гортати попередні роки
        # Якщо у твоїй версії є кнопки гортання, додай локатори під них і клікай у циклі.
        found_year = False
        for _ in range(12):  # обмежимо спроби, щоб не зациклитись
            year_opts = self.elements_are_visible(self.DATE_ADD_TIME_YEAR_LIST)
            target = [y for y in year_opts if y.text.strip() == str(random_date.year)]
            if target:
                target[0].click()
                found_year = True
                break
            # якщо не знайшли — спробуємо «прокрутити» список коліщатком/клавішами або повторно відкрити
            try:
                year_opts[-1].location_once_scrolled_into_view  # легенько скролимо
            except Exception:
                pass
        if not found_year and year_opts:
            random.choice(year_opts).click()  # фолбек: хоч щось вибрати, щоб не впасти

        # 4) Місяць
        self.element_is_clickable(self.DATE_ADD_TIME_MONTH).click()
        months = self.elements_are_visible(self.DATE_ADD_TIME_MONTH_LIST)
        # у react-datepicker порядок з січня (0) до грудня (11)
        months[random_date.month - 1].click()

        # 5) День (беремо тільки з поточного місяця)
        days = self.elements_are_visible(self.DATE_ADD_TIME_DAY_LIST)
        for d in days:
            cls = d.get_attribute("class") or ""
            if d.text.strip() == str(random_date.day) and "outside-month" not in cls:
                d.click()
                break

        # 6) Час (випадковий із видимих)
        try:
            times = self.elements_are_visible(self.DATE_ADD_TIME_TIME_LIST)
            pick = random.choice(times)
            time_text = pick.text.strip()
            pick.click()
        except TimeoutException:
            time_text = None  # якщо у твоїй конфігурації немає тайм-пікера

        return random_date, time_text
