'''
Using tutorial from:
https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
'''

# Importing relevant libraries
import requests
from bs4 import BeautifulSoup as bs

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
    print(swellClean)

    ### TIDE TIMES ###
    
    tideTime = []
    tideType = []

    tide = soup.findAll(class_="table table-sm table-striped table-inverse table-tide")
    for t in tide[0]:
        tText = t.get_text()
        tSplit = tText.split(' ')
        tClean = remove_all(tSplit, '')
        if len(tClean) == 3:
            tideTime.append(tClean[1])
            tideType.append(tClean[0])

    tidesToday = {'type': tideType, 'time': tideTime}
    print(tidesToday)

    '''
    To obtain other information use function soup.findAll,
    then right click on tag required when inspecting web page,
    then copy -> copy element,
    paste into argument of findAll and add an underscore to end of class.
    '''
