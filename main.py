import pandas as pd
import selenium 
import re
from bs4 import BeautifulSoup
import requests
from config import API_KEY
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



"""
-- the objective is to output a dataset in the form of a csv file 
-- 1: make a call to Alpha Vantage API to get PLTR's stock price 
-- 2: scrape US Government Spending webpage to return all contracts awarded to PLTR 
-- 3: merge the data by matching alpha vintage's date and us gov's contract date 
** note: By accident I deleted the code for retrieving data from step 2 but prior to the accident I have stored the output in contracts_data.csv

"""

#make a call to Alpha Vantage API

def fetch_stock_prices():
 url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=PLTR&outputsize=full&apikey={API_KEY}'
 response = requests.get(url)
 if response.status_code == 200: 
  data = response.json()
  return data
 
data = fetch_stock_prices()

def process_stock_data(data):
    time_series = data.get("Time Series (Daily)", {})
    
    rows = []
    
    for date, values in time_series.items():
        row = {
            "Date": date,
            "Open": values["1. open"],
            "High": values["2. high"],
            "Low": values["3. low"],
            "Close": values["4. close"],
            "Volume": values["5. volume"],
        }
        rows.append(row)
    
    df = pd.DataFrame(rows)
    return df

stock_data = process_stock_data(data)
stock_data.to_csv('pltr_stock_prices.csv', index=False)


def format_stock_data(data):
    for date, values in data.items():
        print(f"Date: {date}")
        for key, value in values.items():
            print(f"  {key}: {value}")
        print()  

# Call the function
format_stock_data(data)

#scrape the webpage

def scrape_contracts():
   #need to set up Chrome b/c Selenium essentially automate the process of opening the url on the browser and fetch the data like a browser does.
   #initialize WebDriver
   driver = webdriver.Chrome()
   url = 'https://www.usaspending.gov/keyword_search/palantir'
   driver.get(url)
   #wait for dynamic contents to load: 
   #scroll down since this page contains lazy loaded content 
   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'award-result-generic-cell')))
   #WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'award-result-generic-cell'))

   #class that contains all relevant elements we're looking for: 'award-result-generic-cell'
   contract_cells = driver.find_elements(By.CLASS_NAME, 'award-result-generic-cell') #retrieve all elements that have this class name
   # Print the number of contract cells found
   print(f"Number of contract cells found: {len(contract_cells)}") 
   for cell in contract_cells:
      print(cell.text.strip())
   print(f"Number of contract cells found: {len(contract_cells)}") 

#scrape_contracts()

def merge_data(stock_data):
 contracts_df = pd.read_csv('contracts_data.csv')  # Replace with your actual filename
 stock_data['Date'] = pd.to_datetime(stock_data['Date'])
 contracts_df['Date'] = pd.to_datetime(contracts_df['Date'])
 merged_df = pd.merge(stock_data, contracts_df, on='Date', how='outer')
 #merged_df.to_csv('merged_data.csv', index=False)
 print("Merged data saved to merged_data.csv")
 return merged_df


contracts_df = pd.read_csv('contracts_data.csv')
merged_df = merge_data(stock_data)

"""
def clean_merged_df(merged_df):
   #compute delta of open and close
   #sort dates in descending manner 
   merged_df['Delta Close - Open'] = int(merged_df['Close']) - int(merged_df['Open'])
   merged_df['Delta High - Low'] = int(merged_df['High']) - int(merged_df['Low'])
   sorted_merged_df = merged_df.sort_values(by='Date', ascending=False)
   sorted_merged_df.to_csv('merged_data_cleaned.csv', index=False)


clean_merged_df(merged_df)
"""







   
 
 






