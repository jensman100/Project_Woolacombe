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
import platform

# Defining functions
def remove_all(list, element):
# Removes all instances of element in list
    l = []
    for e in list:
        if e != element:
            l.append(e)
    return l

def find_computer():
    return platform.node()

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
            tidesToday[tClean[1]] = tClean[0]

    '''
    To obtain other information use function soup.findAll,
    then right click on tag required when inspecting web page,
    then copy -> copy element,
    paste into argument of findAll and add an underscore to end of class.
    '''

    ### WRITING TO CSV ###

    computer = find_computer()

    if computer == 'LAPTOP-189M7RS5':
        path_ = r"C:\Users\joeh2\OneDrive\Documents\Project Woolacombe\Code\wave_data.csv"
    else:
        raise Exception('Computer not recognised, please choose path for CSV save')
    
    '''
    Tests what computer is being used so that it saves to the correct location
    Please add in location and computer if using a new device
    Can do this by running platform.node() in python code
    '''

    now_date = datetime.now().strftime("%d/%m/%Y")
    now_time = datetime.now().strftime("%H:%M")


    # Time until high/low tide

    '''
    Time is 24 hour, hh:mm -> need to split by colon to get hours and minutes
    Tides is 12 hours hh:mmXM -> need to split by colon, look at [2] to change hours

    Subtract Time from Tides, first positive number is going to be next
    If none are positive then need to find first tide of next day 
    
    
    '''

    csv_data = {'Date': now_date,'Time': now_time, 'Swell': swellClean}
    csv_data.update(tidesToday)

    headersCSV = list(csv_data.keys())

    print(csv_data)

    with open(path_, 'a', newline='') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=headersCSV)
        dictwriter_object.writerow(csv_data)
        f_object.close()

    print('Complete')