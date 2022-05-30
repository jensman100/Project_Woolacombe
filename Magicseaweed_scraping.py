'''
Using tutorial from:
https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
'''

# Importing relevant libraries
import requests
from bs4 import BeautifulSoup as bs

# Website which data is scraped from
url = 'https://magicseaweed.com/Woolacombe-Surf-Report/1352/'

# Obtaining the the html
page = requests.get(url)
# print(page) # will start with 2 if success, 4 or 5 is bad 

# Makes it readable for python
soup = bs(page.content, 'html.parser')

# Obtaining current swell data
swell = soup.findAll(class_ ="rating-text text-dark")[0] # 2 instaces of the class, want first which is current condition
swellText = swell.get_text() # Extract text data
# print(swellText)

'''
To obtain other information use function soup.findAll,
then right click on tag required when inspecting web page,
then copy -> copy element,
paste into argument of findAll and add an underscore to end of class.
'''
