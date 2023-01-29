from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import string
import time

# Create a webdriver instance
# options = Options()
# options.add_argument("-headless")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# Go to the website
driver.get("https://sell.remixshop.com/pl/sell/select-brand")

# Wait for cookie acceptance element to be present
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Tak, zgadzam się')]"))
    )
    # click the "Accept" button
    element.click()
    time.sleep(3)

finally:

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Męskie')]"))
    )
    # click the "Accept" button
    element.click()
time.sleep(1)
# Find the search field
search_field = driver.find_element("id", "brands-autocomplete")

# Wait for the suggestions to appear
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "brands-autocomplete"))
    )
    time.sleep(3)

finally:

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "autocomplete-list "))
    )
    suggestions = driver.find_elements(By.CLASS_NAME, "autocomplete-list ")

    # Extract the text from each suggestion and save it
    results = []
    for suggestion in suggestions:
        results.append(suggestion.text)

# type into the search field
search_field.send_keys("ab")

# your script to scrape information from the search results goes here
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# extract the search results from the HTML
search_results = soup.find_all("div", class_="autocomplete-list ")

# save the search results to a file
with open("search_results.txt", "wb") as file:
    for result in search_results:
        file.write(result.text)


# Print the results
# print(results)
time.sleep(5)
# Close the driver
driver.quit()
