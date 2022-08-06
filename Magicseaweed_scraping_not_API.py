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

    ### CURRENT SWELL ###

    swell = soup.findAll(class_ ="rating-text text-dark")[0] # 2 instaces of the class, want first which is current condition
    swellText = swell.get_text() # Extract text data
    swellSplit = swellText.split(' ')
    swellClean = swellSplit[4]
    # print(swellClean)

    ### TIDE TIMES ###
    
    tideTime = []
    tideType = []

    tidesToday = {}

    tide = soup.findAll(class_="table table-sm table-striped table-inverse table-tide")
    for t in tide[0]:
        tText = t.get_text()
        tSplit = tText.split(' ')
        tClean = remove_all(tSplit, '')

        if len(tClean) == 3:
            tidesToday[tClean[1]] = tClean[0], tClean[1]

    # print(tidesToday)

    '''
    To obtain other information use function soup.findAll,
    then right click on tag required when inspecting web page,
    then copy -> copy element,
    paste into argument of findAll and add an underscore to end of class.
    '''

    ### WRITING TO CSV ###

    now = datetime.now().strftime("%d/%m/%Y %H:%M")

    csv_data = {'time': now, 'swell': swellClean}
    csv_data.update(tidesToday)

    headersCSV = list(csv_data.keys())

    print(csv_data)

    with open(r'C:\Users\joeh2\OneDrive\Documents\Project Woolacombe\data.csv', 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        dictwriter_object.writerow(csv_data)
        f_object.close()
