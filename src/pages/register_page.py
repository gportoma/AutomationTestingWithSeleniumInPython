from selenium.webdriver.common.by import By
from src.core.action_helper import ActionHelper

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.action_helper = ActionHelper(driver)
        self.first_name = (By.XPATH, "//input[@placeholder='First Name']")
        self.last_name = (By.XPATH, "//input[@placeholder='Last Name']")
        self.address = (By.XPATH, "//textarea[@ng-model='Adress']")
        self.email_address = (By.XPATH, "//input[@ng-model='EmailAdress']")
        self.phone = (By.XPATH, "//input[@type='tel']")
        self.gener_male = (By.XPATH, "//input[@type='radio'][@value='Male']")
        self.hobbies = (By.XPATH, "//div[@class='col-md-4 col-xs-4 col-sm-4']//input[@id='checkbox1']")
        self.skills = (By.XPATH, "//select[@id='Skills']")
        self.countries = (By.ID, "countries")
        self.country = (By.ID, "country")
        self.year_birth = (By.ID, "yearbox")
        self.month_birth = (By.XPATH, "//select[@placeholder='Month']")
        self.day_birth = (By.ID, "daybox")
        self.first_password = (By.ID, "firstpassword")
        self.confirm_password = (By.ID, "secondpassword")
        self.submit_button = (By.ID, "submitbtn")
        self.dropdown_switch_to = (By.XPATH, "//a[text()='SwitchTo']")
        self.frames_link = (By.XPATH, "//a[@href='Frames.html']")
        self.dropdown_widgets = (By.XPATH, "//a[text()='Widgets']")
        self.date_picker_link = (By.XPATH, "//a[@href='Datepicker.html']")
        self.slider_link = (By.XPATH, "//a[@href='Slider.html']")

    def open_browser(self):
        self.driver.get("https://demo.automationtesting.in/Register.html")

    def type_complete_name(self, first_name, last_name):
        self.action_helper.type(self.first_name, first_name)
        self.action_helper.type(self.last_name, last_name)

    def type_address(self, address):
        self.action_helper.type(self.address, address)

    def type_email_addres(self, email_address):
        self.action_helper.type(self.email_address,email_address)

    def type_phone(self, phone):
        self.action_helper.type(self.phone,phone)

    def click_gener_male(self):
        self.action_helper.click(self.gener_male)

    def click_hobbies(self):
        self.action_helper.click(self.hobbies)

    def select_skills(self, text):
        self.action_helper.select_by_visible_text(self.skills, text)

    def select_country(self, text):
        self.action_helper.select_by_visible_text(self.country, text)

    def type_date_birth(self, year, month, day):
        self.action_helper.select_by_visible_text(self.year_birth, year)
        self.action_helper.select_by_visible_text(self.month_birth, month)
        self.action_helper.select_by_visible_text(self.day_birth, day)

    def type_password(self, password):
        self.action_helper.type(self.first_password, password)
        self.action_helper.type(self.confirm_password, password)
        
    def click_submit_button(self):
        self.action_helper.click(self.submit_button)
        
    def navigate_to_frames(self):
        self.action_helper.click(self.dropdown_switch_to)
        self.action_helper.click(self.frames_link)
        
    def navigate_to_date_picker(self):
        self.action_helper.click(self.dropdown_widgets)
        self.action_helper.click(self.date_picker_link)
        
    def navigate_to_slider(self):
        self.action_helper.click(self.dropdown_widgets)
        self.action_helper.click(self.slider_link)
    