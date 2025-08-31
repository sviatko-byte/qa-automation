from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from faker import Faker

from pages.base_page import BasePage


class DatePicker(BasePage):
    DATE_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, ".react-datepicker__month-select")
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, ".react-datepicker__year-select")
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div.react-datepicker__day')

    DATE_ADD_TIME_INPUT = (By.ID, "dateAndTimePickerInput")
    DATE_ADD_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_ADD_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_ADD_TIME_LIST = (By.CSS_SELECTOR, 'react-datepicker__time-list-item ')
    DATE_ADD_TIME_MONTH_LIST = (By.CSS_SELECTOR, "div.react-datepicker__month-option")
    DATE_ADD_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


    fake_en = Faker("en_US")

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
        # Випадкова дата
        random_date = self.fake_en.date_of_birth(minimum_age=18, maximum_age=60)
        print(f"[DEBUG] Generated random_date: {random_date}")

        # Клік по інпуту
        self.element_is_clickable(self.DATE_ADD_TIME_INPUT).click()

        # Вибір року
        self.element_is_clickable(self.DATE_ADD_TIME_YEAR).click()
        years = self.elements_are_visible(self.DATE_ADD_TIME_YEAR_LIST)
        for year in years:
            if year.text == str(2025):
                year.click()
                break

        # Вибір місяця
        self.element_is_clickable(self.DATE_ADD_TIME_MONTH).click()
        # чекаємо поки з'являться місяці
        months = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.DATE_ADD_TIME_MONTH_LIST)
        )
        months[random_date.month - 1].click()

        # Вибір дня
        days = self.elements_are_visible(self.DATE_SELECT_DAY_LIST)
        for day in days:
            if day.text == str(random_date.day) and "outside-month" not in day.get_attribute("class"):
                day.click()
                break

        # Вибір часу
        times = self.elements_are_visible(self.DATE_ADD_TIME_LIST)
        random_time_element = random.choice(times)
        random_time = random_time_element.text
        random_time_element.click()

        return random_date, random_time