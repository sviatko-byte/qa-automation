import os
import time
from data.constans import DefaultConstants, Urls
from utils.helpers import (
    is_file_downloaded,
    create_random_file,
    generate_random_name,
    generate_random_email,
    generate_random_mobile,
)


def test_search_and_login(pages):
    pages.base_page.open(Urls.COURSEHUNTER)
    pages.main_page.click_on_sign_in_btn()
    pages.main_page.fill_email(DefaultConstants.login)
    pages.main_page.fill_password(DefaultConstants.password)
    pages.main_page.click_on_sign_in()
    time.sleep(3)
    pages.main_page.log_out(pages.base_page.driver)


def test_different_click_on_the_buttons(pages):
    pages.base_page.open(Urls.BUTTONS)
    pages.buttons_page.double_click()
    pages.buttons_page.should_display_double_click_message('You have done a double click')
    pages.buttons_page.right_click()
    pages.buttons_page.should_display_right_click_message('You have done a right click')


def test_check_link(pages):
    pages.base_page.open(Urls.LINKS)
    pages.links_page.check_new_tab_simple_link()


def test_broken_link(pages):
    pages.base_page.open(Urls.LINKS)
    pages.links_page.check_broken_link()


def test_download(pages):
    pages.base_page.open(Urls.DOWNLOAD)
    pages.download_page.click_on_download_btn()
    full_path = os.path.join(DefaultConstants.download_dir, DefaultConstants.filename)
    assert is_file_downloaded(full_path)


def test_upload(pages):
    pages.base_page.open(Urls.UPLOAD)
    path = create_random_file(DefaultConstants.download_dir)
    pages.download_page.upload_file(path)
    pages.download_page.should_be_visible_success_upload_message()


def test_dynamic_properties_page(pages):
    pages.base_page.open(Urls.DYNAMIC_PROPERTIES)
    pages.dynamic_properties_page.check_changed_color()


def test_form(pages):
    pages.base_page.open(Urls.FORM)
    random_name = generate_random_name(length=6)
    random_email = generate_random_email(length=8)
    random_mobile = generate_random_mobile()

    pages.form_page.fill_form_fields(
        name=random_name,
        last_name=random_name,
        email=random_email,
        mobile=random_mobile,
    )
    pages.form_page.select_state('NCR')
    pages.form_page.select_city('Noida')
    pages.form_page.click_on_submit_btn()


def test_browser_window(pages):
    pages.base_page.open(Urls.BROWSER_WINDOW)
    pages.browser_window.click_on_submit_btn()
    pages.browser_window.switch_to_window(1)
    pages.browser_window.get_page_title()
    pages.browser_window.switch_to_window(0)
    pages.browser_window.click_on_new_window_btn()
    pages.browser_window.switch_to_window(1)
    pages.browser_window.get_on_new_window_title()


def test_alerts_page(pages):
    pages.base_page.open(Urls.ALERTS)
    alerts_text = pages.alerts_page.check_see_alert()
    pages.alerts_page.accept_alert()
    assert alerts_text == 'You clicked a button'

    alerts_text = pages.alerts_page.check_alert_appear_5_sec()
    assert alerts_text == 'This alert appeared after 5 seconds'
    pages.alerts_page.accept_alert()

    text_result = pages.alerts_page.check_confirm_box()
    assert text_result == 'You selected Ok'

    text_result = pages.alerts_page.check_prompt_box()
    assert text_result


def test_frames_page(pages):
    pages.base_page.open(Urls.FRAMES)
    result_frame1 = pages.frames_page.check_frames("frame1")
    result_frame2 = pages.frames_page.check_frames("frame2")
    print(result_frame1, result_frame2)


def test_nested_frames_page(pages):
    pages.base_page.open(Urls.NESTED_FRAMES)
    parent_text, child_text = pages.nested_frames_page.check_nested_frames_page()
    print(parent_text, child_text)


def test_modal_dialogs_page(pages):
    pages.base_page.open(Urls.MODAL_DIALOGS)
    small, large = pages.modal_dialogs_page.small_modal_modal()
    print(small)
    print(large)


def test_widgets_page(pages):
    pages.base_page.open(Urls.WIDGETS)
    pages.widgets_page.check_accordian(accordian_num='first')
    pages.widgets_page.check_accordian(accordian_num='second')
    pages.widgets_page.check_accordian(accordian_num='third')


def test_autocomplete_page(pages):
    pages.base_page.open(Urls.AUTO)
    pages.auto_complete.fill_input_multi()
    pages.auto_complete.fill_input_multi()
    pages.auto_complete.fill_input_multi()
    count_after, count_before = pages.auto_complete.remove_value_from_multi()
    print(f"Before removal: {count_before}, After removal: {count_after}")


def test_date_picker_page(pages):
    pages.base_page.open(Urls.DATE_PICKER)
    random_date = pages.date_picker.select_date()
    date_input_value = pages.date_picker.element_is_visible(pages.date_picker.DATE_INPUT).get_attribute("value")
    expected_date_str = random_date.strftime("%m/%d/%Y")
    print(f"Expected: {expected_date_str}, Got from input: {date_input_value}")
    assert date_input_value == expected_date_str


def test_date_and_time_picker(pages):
    pages.base_page.open(Urls.DATE_TIME_PICKER)
    pages.date_picker.select_date_and_time()


def test_slider_page(pages):
    pages.base_page.open(Urls.SLIDER)
    before, after = pages.slider.change_slider_value()
    print(f"Before: {before}, After: {after}")


def test_progress_bar_page(pages):
    pages.base_page.open(Urls.PROGRES_BAR)
    before, after = pages.progress_bar.progress_bar_click()
    print(before, after)


def test_tabs_page(pages):
    pages.base_page.open(Urls.TABLES)
    pages.tables.check_tabs()


def test_tooltips_page(pages):
    pages.base_page.open(Urls.TOOL_TIPS)
    button_text, field_text, contrary_text, section_text = pages.tooltips.check_tool_tips()
    print(button_text, field_text, contrary_text, section_text)


def test_menu_page(pages):
    pages.base_page.open(Urls.MENU)
    pages.menu.check_menu()


def test_select_menu(pages):
    pages.base_page.open(Urls.SELECT_MENU)
    pages.select_menu.select_option_by_text("Group 1, option 1")
    pages.select_menu.select_title_by_text("Dr.")
    pages.select_menu.select_random_color()
    pages.select_menu.multiselect_drop_by_text("Red")
    pages.select_menu.select_car_by_name("Volvo")
