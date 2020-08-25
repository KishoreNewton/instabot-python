from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os 
import time

# This class uses selenium to open browser and automate 
class InstagramBot:

    def __init__(self, username, password):
        """
        Args:
            username:str: Instagram's username
            password:str: Instagram's password

        Chromedriver location at root of folder
        """
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver')
        self.base_url = 'https://www.instagram.com'
        self.login()

    def login(self):
        self.driver.get(f'{self.base_url}/accounts/login/')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(self.username)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(self.password)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div'))).click()
        time.sleep(3)
    
    def nav_user(self, user):
        self.driver.get(f'{self.base_url}/{user}')

    def follow_user(self, user):
        """
        navigate the user and follow them
        """
        self.nav_user(user)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/a/button'))).click()
        time.sleep(30)
        self.unfollow_user(user)

    def unfollow_user(self, user):
        """
        navigate the user and unfollow them
        """
        self.nav_user(user)
        self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/a/button'))).click()
    

if __name__ == '__main__':
    """
    Args:
        id_bot initialize the class InstagramBot with username and password 
        ig_bot.follow_user enter the user to follow and unfollow

    """
    ig_bot = InstagramBot('temp_username', 'temp_password')

    ig_bot.follow_user('tonyrobbins')
