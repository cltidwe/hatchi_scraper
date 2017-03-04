url = "http://www.toysrus.com/product/index.jsp?productId=96165816&cp=2255956.3209580.99530216&parentPage=family"
r = requests.get(url)

soup = BeautifulSoup(r.content)

table = soup.find_all("div", {"id": "productPanel"})
for item in table:
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