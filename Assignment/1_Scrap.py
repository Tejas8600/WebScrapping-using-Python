from bs4 import BeautifulSoup
import requests
from csv import writer


url="https://housing.com/in/buy/searches/P3zgy19bgb2xjywqp"
page = requests.get (url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="css-1nr7r9e")


with open('Housing.csv', 'w', encoding='utf8', newline='') as f:
     thewriter =writer(f)
     header = ['Title', 'Location', "Price", 'Avg_price' ]
     thewriter.writerow(header)

     for list in lists:
         Title = list.find('a', class_="css-15n0x03").text
         Location = list.find('a', class_="css-xkwyom").text
         Price = list.find('div', class_="css-18rodr0").text
         Avg_price = list.find('div', class_="css-4z3njv").text
         info = [Title, Location, Price, Avg_price]
         print(info)
         thewriter.writerow(info)
