from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.utils.config_loader import load_config

config = load_config()

def get_driver():
    driver_path = config['webdriver']['path']
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver
