# terminal: python skyscanner.py

from bs4 import BeautifulSoup
import requests
import json
import re
from selenium import webdriver
import pandas as pd


driver = webdriver.Firefox()
# Gets source code
driver.get("https://www.skyscanner.com/transport/flights/nyca/mkca?adults=1&children=0&adultsv2=1&childrenv2=&infants=0&cabinclass=economy&rtn=0&preferdirects=false&outboundaltsenabled=false&inboundaltsenabled=false&oym=1903&selectedoday=19/")

# converts java to HTML (i think)
html = driver.execute_script("return document.documentElement.outerHTML")

# parses the HTML
sel_soup = BeautifulSoup(html, 'html.parser')

# this finds everything with the class="date"
# print(sel_soup.select(".date"))
#
# # tag with a class!!!
# print(sel_soup.select("div.date"))
# print("-"*20)
# print(sel_soup.select("div.price"))

#does the same thing as above just with find_all
# print(sel_soup.finda_all("div", class_="date"))

prices = [p.get_text() for p in sel_soup.select("div.price")]
print("-"*20)
# print(prices)
# print(len(prices))


dates = [d.get_text() for d in sel_soup.select("div.date")]
print("-"*20)
# print(dates)
# print(len(dates))



weather = pd.DataFrame({
        "Days of the Month": dates,
        "Prices": prices
})
weather.index.name = 'index'

print(weather)
