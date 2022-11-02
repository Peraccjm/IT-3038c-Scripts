from urllib import request
from bs4 import BeautifulSoup
import requests, re

url = "https://angelty.pe/collections/items/products/end-knitted-pullover"
html = request.urlopen(url).read().decode('utf8')
html[:60]

soup = BeautifulSoup(html, 'html.parser')
title = soup.find('title')

h1 = soup.find('h1' , {'class' : 'product-title-block mt-4 break-words font-heading text-2xl lg:text-5xl'})
price = soup.find('span', { 'class':"money data-currency-usd="})



print('The name of the item is', title)
