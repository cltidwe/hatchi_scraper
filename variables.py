#////	* * * * *  WALMART 
import requests
from bs4 import BeautifulSoup

url = "https://www.walmart.com/search/?query=hatchimals"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.contents[1].find_all("a", {"class": "js-product-title"})[0].text
	price = item.contents[3].find_all("span", {"class": "price"})[0].text
	stock = item.contents[3].find_all("span", {"class": "price-auxblock"})[0].text

#////	*# ITEM 1  Hatchimals Draggles Blue/Green Egg


url = "http://www.toysrus.com/product/index.jsp?productId=88534486&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text

#////	# ITEM 2 Hatchimals Owlicorn Pink/Blue Egg

import requests
from bs4 import BeautifulSoup

url = "http://www.toysrus.com/product/index.jsp?productId=96165816&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text


#////	* * * * *  ITEM 3 # Hatchimals Pengualas Pink/Teal Egg

import requests
from bs4 import BeautifulSoup

url = "http://www.toysrus.com/product/index.jsp?productId=96165806&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text

#////	* * * * *  ITEM 4 # Hatchimals Draggles Blue/Purple Egg

import requests
from bs4 import BeautifulSoup

url = "http://www.toysrus.com/product/index.jsp?productId=105339906&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text

#////	* * * * *  ITEM 5 # Hatchimals Pengualas Pink Egg

import requests
from bs4 import BeautifulSoup

url = "http://www.toysrus.com/product/index.jsp?productId=88534376&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

g_data = soup.find_all("div", {"class": "tile-content"})

for item in g_data:
	title = item.find_all("div", {"id": "lTitle"})[0].h1.text
	price = item.find_all("li", {"class": "retail"})[0].text
	stock = item.find_all("div", {"id": "productOOS"})[0].text

