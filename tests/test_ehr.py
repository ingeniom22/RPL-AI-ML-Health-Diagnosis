import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import time

load_dotenv()

USER_URL = os.getenv("USER_URL")
USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")

class UserCreateEHR(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver
        driver.get(USER_URL)

        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        username_field.send_keys(USER_EMAIL)
        password_field.send_keys(USER_PASSWORD)

        login_button.submit()

        time.sleep(5)
        self.assertIn("Doc.ai", driver.page_source)

        driver.get(USER_URL + "/ehr")
        time.sleep(5)

        driver.get(USER_URL + "/ehr-add")
        time.sleep(5)

        self.assertIn("Add Data", driver.page_source)
        time.sleep(5)
        
        title_field = driver.find_element(By.NAME, "title")
        content_field = driver.find_element(By.NAME, "content")
        published_field = driver.find_element(By.NAME, "published")
        time.sleep(5)
        
        title_field.send_keys("ada kok")
        content_field.send_keys("ini buat test content")
        driver.execute_script("arguments[0].click();", published_field)
        time.sleep(5)
        
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.submit()
        time.sleep(5)
        

        

    def tearDown(self):
        self.driver.close()
