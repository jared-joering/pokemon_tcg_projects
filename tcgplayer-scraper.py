# TODO: !!! modularize this code into functions and classes !!!
# TODO: add a bulk entry option for cards
# TODO: implement a better wait method instead of implicitly waiting

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# set up the FireFox driver, its options, and practice url
url_input = input("Enter the TCGPlayer URL: ")
driver = webdriver.Firefox()

# load the user-supplied webpage
driver.get(url_input)

# obligatory wait
driver.implicitly_wait(5)

# find the '1Y' (1 year) button and click it so that we can get the history for the last 12 months
driver.find_element(By.XPATH, "//button[contains(text(), '1Y')]").click()

# find the name, set, card number, and rarity of the card
card = driver.find_element(By.XPATH, "//span[@data-testid='lnkProductSearchSet']").text
set = driver.find_element(By.XPATH, "//a[@data-testid='lnkProductDetailsSetName']").text
number = driver.find_element(By.XPATH, "//span[@data-v-7d56df22='']").text.split(" / ")[0]  # splitting between the /
rarity = driver.find_element(By.XPATH, "//span[@data-v-7d56df22='']").text.split(" / ")[1]
volatility = driver.find_element(By.XPATH, "//span[@data-v-6bf6748f='']").text
condition = " ".join(driver.find_element(By.XPATH, "//section[@class='spotlight__condition']").text.split(" ")[:2]) # pulling the first two words 'Near Mint', 'Lightly Played', etc.
if "Damaged" in condition: # TODO: a very basic check for damaged cards, but it works for now
    condition = "Damaged"

# inserting Beautiful Soup to parse the page source since Selelnium wasn't able
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# another wait
driver.implicitly_wait(3)

# creating a date and price list to store the data we want to extract
dates = []
prices = []

# using bs to find the table body that contains the price history
rows = soup.select("tbody[data-v-43dee7cd] tr")

# create a simple for loop to iterate through each row and extract the data
for row in rows:
    object = row.find_all("td") # locating the first td we need to start pulling data from
    if object:
        date = object[0].get_text(strip=True)   # getting (and cleaning) the date
        price = object[1].get_text(strip=True)  # and the price too
        
        try:    # converting the price to a float so that we can do calculations later
            price = float(price.replace("$", "").replace(",", "")) # removing the dollar sign and commas
        except ValueError:
            price = 0.0 # had to set this up because some cards have been recently released, so they don't have pricing data before they were actually on market

        dates.append(date)
        prices.append(price)

# open a csv file in append mode and write the data to it
with open('tcgplayer-data.csv', 'a+', newline='') as csvfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(csvfile)
    csvfile.seek(0) # move to the very beginning to set up a check if the header is blank
    
    if list(reader) == []:  # check if the header is there or not
        writer.writerow(['Card', 'Set', 'Number', 'Rarity', 'Condition', 'Volatility'] + dates) # if not, write the header
    
    writer.writerow([card, set, number, rarity, condition, volatility] + [f"{price:.2f}" for price in prices]) # regardless of whether or not the header's there, write the card data

driver.quit() # closing the browser

print("Data extraction complete. Check 'tcgplayer-data.csv' for results.") # let the user know that the script has finished running