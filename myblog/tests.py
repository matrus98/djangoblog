import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element(By.XPATH, '//*[@id="id_username"]').send_keys("testuser")
    driver.find_element(By.XPATH, '//*[@id="id_password"]').send_keys("p4ssword")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[3]/input').click()

element_is_clickable()
