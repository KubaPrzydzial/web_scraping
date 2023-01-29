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

# create a webdriver instance (had to do it this way, otherwise driver not compatible with os (???)

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

# go to website
driver.get("https://secret.website/")

# wait for cookie popup
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Tak, zgadzam się')]"))
    )
    # accept cookies
    element.click()
    # not neccesary but sometimes script acts iffy
    time.sleep(3)

finally:

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'category-of-your-choice')]"))
    )
    # press category of your choice
    element.click()

time.sleep(1)
# find the search field
search_field = driver.find_element("id", "brands-autocomplete")

# wait fot the suggestion to appear
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

    alphabet = string.ascii_lowercase
    for letter1 in alphabet:
        for letter2 in alphabet:
            # type the combination of 2 letter into the search field
            search_field.send_keys(letter1 + letter2)
            # wait for the page to load
            wait = WebDriverWait(driver, 10)
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "autocomplete-list ")))
            # save results here
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            # save results from html
            search_results = soup.find_all("div", class_="autocomplete-list")

            # save the search results to a file
            with open("search_results.txt", "a", encoding="utf-8") as file:
                for result in search_results:
                    file.write(result.text + '\n')
            search_field.clear()

# not necessary but I want to see something
time.sleep(5)
# close the browser
driver.quit()
