### CURRENTLY CANNOT WRITE AS NEED AN API KEY
### HAVE REQUESTED BY EMAIL - 05/08/22


'''
Using tutorials from:
https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
https://www.delftstack.com/howto/python/python-append-to-csv/
'''

# Importing relevant libraries
import requests
from bs4 import BeautifulSoup as bs
from csv import DictWriter
from datetime import datetime

# Defining functions
def remove_all(list, element):
# Removes all instances of element in list
    l = []
    for e in list:
        if e != element:
            l.append(e)
    return l

### MAIN CODE ###
if __name__ == '__main__':

    # Website which data is scraped from
    url = 'https://magicseaweed.com/Woolacombe-Surf-Report/1352/'

    # Obtaining the the html
    page = requests.get(url)
    # print(page) # will start with 2 if success, 4 or 5 is bad 

    # Makes it readable for python
    soup = bs(page.content, 'html.parser')