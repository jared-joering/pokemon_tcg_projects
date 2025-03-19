import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# set up the FireFox driver, its options, and url
url = "https://www.tcgplayer.com/product/165734?Language=English&Condition=Near+Mint&page=1" # url_input = input("Enter the TCGPlayer URL: ")
driver = webdriver.Firefox()

# load the webpage
driver.get(url) # driver.get(url_input)

# wait for the page to load
driver.implicitly_wait(5)

# find the '1Y' button and click it so that we can get the history for the last 12 months
driver.find_element(By.XPATH, "//button[contains(text(), '1Y')]").click()

# find the name, set, card number, and rarity of the card
'''<ul data-v-7d56df22="" class="product__item-details__attributes"><li data-v-7d56df22=""><div data-v-7d56df22=""><strong data-v-7d56df22="">Card Number / Rarity:</strong><span data-v-7d56df22="">124/131 / Ultra Rare</span></div>'''

card = driver.find_element(By.XPATH, "//span[@data-testid='lnkProductSearchSet']").text
set = driver.find_element(By.XPATH, "//a[@data-testid='lnkProductDetailsSetName']").text
number = driver.find_element(By.XPATH, "//span[@data-v-7d56df22='']").text.split(" / ")[0] # retrieving the card number alone
rarity = driver.find_element(By.XPATH, "//span[@data-v-7d56df22='']").text.split(" / ")[1] # retrieving the rarity

driver.implicitly_wait(3)

# create a variable to allow beautiful soup to parse the page source
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# create a date and price list to store the data we want to extract
dates = []
prices = []

# using beautiful soup to find the table body that contains the price history
rows = soup.select("tbody[data-v-43dee7cd] tr")

# create a simple for loop to iterate through each row and extract the data
for row in rows:
    object = row.find_all("td") # locating the table we need to pull data from
    if object:
        date = object[0].get_text(strip=True) # getting the date
        price = object[1].get_text(strip=True) # "
        dates.append(date)
        prices.append(price)



# TODO: open a csv file in append mode and write the data to it
# TODO: test this out
# TODO: possibly 



driver.quit()