from bs4 import BeautifulSoup
import requests

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

with open('test.csv', 'w') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow(["Title", "Price", "Stock", "Last updated"])
	for title, price, stock in data:
		writer.writerow([title, price, stock, datetime.now()])