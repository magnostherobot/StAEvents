from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import re
import time
import json
import datetime
from bs4 import BeautifulSoup


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = 'https://events.st-andrews.ac.uk/all-events/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll("div", {"id": re.compile("^event_")})


# Python program to convert time
# from 12 hour to 24 hour format

# Function to convert the date format
def convert24(str1):
    # Checking if last two elements of time
    # is AM and first two elements are 12
    if str1[-2:] == "am" and str1[:2] == "12":
        return "00" + str1[2:-2]
    # remove the AM
    elif str1[-2:] == "am":
        return str1[:-2]
    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif str1[-2:] == "pm" and str1[:2] == "12":
        return str1[:-2]
    else:
        # add 12 to hours and remove PM
        return str(int(str1[:2]) + 12) + str1[2:6]

# Driver Code
#print(convert24("08:05:45 PM"))

for tag in a:
    name = tag.find("span", itemprop="name").text
    info = tag.findAll("em")
    time = info[0].text
    location = info[1].text
    date = tag.find("span", {"class","evcal_desc3"}).text
    dict = {"name": name, "date": date, "time": time, "location": location}
    # print(dict['name'])
    print(name)
    date_obj = datetime.datetime.strptime(date, '%A %d %B %Y')
    date = date_obj.date()
    date = str(date)
    print(date)
    print(time)
    splitted_time = time.split()
    start_time = splitted_time[0]+splitted_time[1]
    splitted_time2 = splitted_time[::-1]
    end_time = splitted_time2[1]+splitted_time2[0]
    # if len(start_time)<6 and len(end_time)<6:
    #     start_time_obj = datetime.datetime.strptime(start_time, '%I:%M:%S%p')
    #     # start_time = start_time_obj.time()
    #     end_time_obj = datetime.datetime.strptime(end_time, '%I:%M:%S%p')
    #     end_time = datetime.strptime(end_time, '%H:%M:%S')
        # end_time = end_time_obj.time()
    datestarttime = date+'T'+start_time
    dateendtime = date+'T'+end_time
    print(datestarttime)
    print(dateendtime)
    print(location)
    print(' ')
