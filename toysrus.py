from bs4 import BeautifulSoup
import requests

#TRU 1
url = "http://www.toysrus.com/product/index.jsp?productId=88534486&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "productPanel"}) 

data = []

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	# save the data in tuple
	data.append((title, price, stock))

import csv  
from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

from bs4 import BeautifulSoup
import requests

#TRU 2
url = "http://www.toysrus.com/product/index.jsp?productId=96165816&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "productPanel"}) 

data = []

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	# save the data in tuple
	data.append((title, price, stock))

import csv  
from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

#TRU 4
url = "http://www.toysrus.com/product/index.jsp?productId=105339906&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

url = "https://www.walmart.com/search/?query=hatchimals"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "productPanel"}) 

data = []

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	# save the data in tuple
	data.append((title, price, stock))

import csv  
from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

from bs4 import BeautifulSoup
import requests

#TRU 5
url = "http://www.toysrus.com/product/index.jsp?productId=88534376&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "productPanel"}) 

data = []

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	# save the data in tuple
	data.append((title, price, stock))

import csv  
from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])

from bs4 import BeautifulSoup
import requests

url = "https://www.walmart.com/search/?query=hatchimals"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"id": "productPanel"}) 

data = []

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text
	# save the data in tuple
	data.append((title, price, stock))

import csv  
from datetime import datetime  

with open('hatchimals.csv', 'w') as csv_file:  
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])