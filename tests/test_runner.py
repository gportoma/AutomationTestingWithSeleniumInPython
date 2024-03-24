import pytest
import time
from src.core.driver_factory import get_driver
from src.pages.register_page import RegisterPage
from src.pages.frame_page import FramePage
from src.pages.date_picker_page import DatePickerPage
from src.pages.slider_page import SliderPage

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_register_form(driver):
    register_page = RegisterPage(driver)
    register_page.open_browser()
    register_page.type_complete_name("Guilherme", "Malta")
    register_page.type_address("Rua Joaquim Guarani, 419, SP")
    register_page.type_email_addres("guilherme-porto7@hotmail.com")
    register_page.type_phone("1135869216")
    register_page.click_gener_male()
    register_page.click_hobbies()
    register_page.select_skills("Java")
    register_page.select_country("Australia")
    register_page.type_date_birth("1999", "October", "11")
    register_page.type_password("qweasd123")
    register_page.click_submit_button()
    time.sleep(3)

def test_type_iframe(driver):
    register_page = RegisterPage(driver)
    frame_page = FramePage(driver)
    register_page.open_browser()
    register_page.navigate_to_frames()
    frame_page.type_in_single_frame("Type in single frame")
    time.sleep(3)
    
def test_select_date_picker_enabled(driver):
    register_page = RegisterPage(driver)
    date_picker_page = DatePickerPage(driver)
    register_page.open_browser()
    register_page.navigate_to_date_picker()
    date_picker_page.type_date_picker_enabled("11/10/1999")
    time.sleep(3)
    
def test_select_date_picker_disabled(driver):
    register_page = RegisterPage(driver)
    date_picker_page = DatePickerPage(driver)
    register_page.open_browser()
    register_page.navigate_to_date_picker()
    date_picker_page.select_birth_date("10/11/1999")
    time.sleep(3)
    
def test_select_50_per_cent_to_slider(driver):
    register_page = RegisterPage(driver)
    slider_page = SliderPage(driver)
    register_page.open_browser()
    register_page.navigate_to_slider()
    slider_page.select_50_percent_in_slider()
    time.sleep(3)