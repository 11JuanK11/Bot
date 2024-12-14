from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
import time


service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
bot.get("https://www.viajesexito.com")

try:
    closeSpam = bot.find_element(By.XPATH, '/html/body/div/div/div/div[1]')
    time.sleep(2)
    closeSpam.click()
    time.sleep(2)
except Exception as e:
    print(f"Ocurrió un error: {e}")



