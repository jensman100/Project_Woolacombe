'''
Using tutorial from:
https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
'''

import requests
from bs4 import BeautifulSoup as bs

url = 'https://magicseaweed.com/Woolacombe-Surf-Report/1352/'

page = requests.get(url)
# print(page) # will start with 2 if success, 4 or 5 is bad 

soup = bs(page.content, 'html.parser')

swell = soup.findAll(class_ ='h4 nomargin msw-js-bind-primary-height' )
print(swell)