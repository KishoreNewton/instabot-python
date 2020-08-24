from selenium import webdriver
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
        self.driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')
