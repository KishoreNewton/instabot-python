from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os 
import time

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        CHROMEDRIVER_PATH = './chromedriver'
        self.driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)
        self.driver.get('https://www.instagram.com/')

if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')

    print(ig_bot.username)
