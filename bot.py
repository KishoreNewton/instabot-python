from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os 
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.login()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(self.username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(self.password)
        # self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))).click()
        # self.driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        # self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        # self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')
