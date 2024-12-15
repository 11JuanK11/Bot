from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EXP_COND
import time


# Configuration and initialization of the bot
service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
bot.get("https://www.viajesexito.com")


# Handle the pop-up when loading the page and close it
load_spam = WebDriverWait(bot , 10).until(
    EXP_COND.presence_of_element_located((By.XPATH, '/html/body/div[6]/div/div/iframe'))
)
bot.switch_to.frame(load_spam)

close_spam = WebDriverWait(bot , 10).until(
    EXP_COND.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[1]'))
)
close_spam.click()   #Cerrar el anuncio

bot.switch_to.default_content()   # Return to the main page
time.sleep(1)


# Go to the Flight + Hotel button
flight_hotel = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[1]/ul/li[3]/a/span')
flight_hotel.click()
time.sleep(1)


# Select and enter the departure airport
text = "José María Cordova"
origin_airport = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origin_airport.click()
time.sleep(1)

origin_airport_text = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
origin_airport_text.send_keys(text)
time.sleep(1)
origin_airport_text.send_keys(Keys.ENTER)
time.sleep(1)


# Select and enter the destination airport
text = "Cancún, Quintana Roo (CUN-Aeropuerto Internacional"
destination_airport = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destination_airport.click()     # Select the input field
time.sleep(1)

destination_airport_text = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destination_airport_text.send_keys(text)    # Enter the destination airport
time.sleep(2)

destination_option = WebDriverWait(bot , 10).until(EXP_COND.element_to_be_clickable((By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div/div[2]/p[2]')))
destination_option.click()  # Select the destination airport
time.sleep(1)


# Select and enter travel dates
date_travels = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
date_travels.click()     # Select the input field
time.sleep(1)

# Enter departure date - Based on the last digit of Sara Sánchez's ID (0)
xpath = "//div[@aria-label='Viernes, Diciembre 20, 2024' and text()='20']"
date_departure_airport = WebDriverWait(bot, 10).until(EXP_COND.presence_of_element_located((By.XPATH, xpath)))
date_departure_airport.click()     # Select the start date
time.sleep(2)

# Enter return date - Based on the last digit of Juan Alzate's ID (4)
xpath2 = "/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[2]/div[6]/div[2]/div[1]"
date_return_airport = WebDriverWait(bot, 10).until(EXP_COND.presence_of_element_located((By.XPATH, xpath2)))
date_return_airport.click()    # Select the end date
time.sleep(1)

accept = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
accept.click()
time.sleep(2)

