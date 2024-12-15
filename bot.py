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

# Add rooms
select_button = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
select_button.click()
time.sleep(1)

# Add a second room and set the number of adults
second_room = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
second_room.click()
time.sleep(1)

add_persons = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button')
actions = ActionChains(bot)
actions.double_click(add_persons).perform() 
time.sleep(1)

send_rooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
send_rooms.click()
time.sleep(2)


# Search results for the query
search = bot.find_element(By.XPATH, '/html/body/form/div[3]/div/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
search.click()
time.sleep(20)


# Go to the new tab
handles = bot.window_handles
bot.switch_to.window(handles[-1])


# Search for all packages
results_container = WebDriverWait(bot, 10).until(EXP_COND.presence_of_element_located((By.ID, 'divAirResults')))
cards = results_container.find_elements(By.XPATH, './div[contains(@class, "row column")]')

# Loop to display package prices in the console
for i, tarjeta in enumerate(cards, 1):
    try:
        travel_prices = tarjeta.find_elements(By.XPATH, './/span[contains(@class, "currencyText")]')

        if len(travel_prices) > 1:
            print(f"Price {i}: {travel_prices[1].text}")
        else:
            print(f"Price {i}: No second price in this option.")

    except Exception as e:
        print(f"Error in card {i}: {e}")


# Go to advanced search
advanced_search = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
advanced_search.click()
time.sleep(1)


# Enter the airline name, selected airline: Avianca
text = "Avianca"
airline_input = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
bot.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", airline_input)   # Scroll down the page
airline_input.send_keys(text)
airline_input.send_keys(Keys.ENTER)
time.sleep(1)


# Search by airline
search = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
search.click()
time.sleep(10)


# Go to "Contact Us" and access the WhatsApp number
bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")     # Scroll to the bottom of the page
time.sleep(5)
whatsApp_button = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[5]/footer/div[2]/div/div/div[1]/div/p[1]/a')
whatsApp_button.click()
time.sleep(5)


bot.close() # Close the bot