#!/usr/local/bin python
from bs4 import BeautifulSoup
import requests
import csv 

url = "https://www.walmart.com/search/?query=hatchimals"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

data = []

for item in g_data:
	title = item.contents[1].find_all("a", {"class": "js-product-title"})[0].text
	price = item.contents[3].find_all("span", {"class": "price"})[0].text
	stock = item.contents[3].find_all("span", {"class": "price-auxblock"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	# The for loop
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

url = "http://www.toysrus.com/product/index.jsp?productId=88534486&cp=2255956.3209580.99530216&parentPage=family"

r = requests.get(url)

soup = BeautifulSoup(r.content)

tables = soup.find_all("div", {"id": "productPanel"})

for item in tables:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Price", "Stock", "Last updated"])
    # The for loop
    for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

url = "http://www.toysrus.com/product/index.jsp?productId=96165816&cp=2255956.3209580.99530216&parentPage=family"

r = requests.get(url)

soup = BeautifulSoup(r.content)

tables = soup.find_all("div", {"id": "productPanel"})

for item in tables:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Price", "Stock", "Last updated"])
    # The for loop
    for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

url = "http://www.toysrus.com/product/index.jsp?productId=96165806&cp=2255956.3209580.99530216&parentPage=family"

r = requests.get(url)

soup = BeautifulSoup(r.content)

tables = soup.find_all("div", {"id": "productPanel"})

for item in tables:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	# The for loop
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

url = "http://www.toysrus.com/product/index.jsp?productId=105339906&cp=2255956.3209580.99530216&parentPage=family"

r = requests.get(url)

soup = BeautifulSoup(r.content)

tables = soup.find_all("div", {"id": "productPanel"})

for item in tables:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	# The for loop
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

url = "http://www.toysrus.com/product/index.jsp?productId=88534376&cp=2255956.3209580.99530216&parentPage=family"

r = requests.get(url)

soup = BeautifulSoup(r.content)

tables = soup.find_all("div", {"id": "productPanel"})

for item in tables:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	data.append((title, price, stock))

from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	# The for loop
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])