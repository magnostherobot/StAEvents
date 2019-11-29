from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import requests
import re
import time
import json
from bs4 import BeautifulSoup
import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=
[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json',
SCOPES)
    creds = tools.run_flow(flow, store, flags) \
          if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http=creds.authorize(Http()))

# Google API stuff
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

url = 'https://events.st-andrews.ac.uk/all-events/'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
a = soup.findAll("div", {"id": re.compile("^event_")})

#dict = {"name": name, "date": date, "time": time, "location": location}
# print(dict["myEventNameOrKey"]["date"])

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
    splitted_time2=splitted_time[::-1]
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

# Adding event to google calendar

    EVENT = {
        'name': dict['name'],
        'start': {'dateTime': 'datestarttime'},
        'end': {'dateTime': 'dateendtime'},
        'location': {'location': location}
    }
    e = CAL.events().insert(calendarId='primary',
                    sendNotifications=True, body=EVENT).execute()

# event = {
#   'summary': 'Google I/O 2015',
#   'location': '800 Howard St., San Francisco, CA 94103',
#   'start': {
#     'dateTime': '2015-05-28T09:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'end': {
#     'dateTime': '2015-05-28T17:00:00-07:00',
#     'timeZone': 'America/Los_Angeles',
#   },
#   'recurrence': [
#     'RRULE:FREQ=DAILY;COUNT=2'
#   ],
#   'attendees': [
#     {'email': 'lpage@example.com'},
#     {'email': 'sbrin@example.com'},
#   ],
#   'reminders': {
#     'useDefault': False,
#     'overrides': [
#       {'method': 'email', 'minutes': 24 * 60},
#       {'method': 'popup', 'minutes': 10},
#     ],
#   },
# }
#
#
# date_time_str = 'Jun 28 2018  7:40AM'
# date_obj = datetime.datetime.strptime(date, '%b %d %Y')
# date=date_obj.date()
# time_obj = datetime.datetime.strptime(date_time_str, '%I:%M%p')
# time=time_obj.time()
#
# # Creating events
#
# EVENT2 = {
#     'summary': 'Buy Bannanas',
#     'start': {'dateTime': '2019-11-25T13:00:00%s' % GMT_OFF},
#     'end': {'dateTime': '2019-11-25T14:00:00%s' % GMT_OFF},
# }
#
# e = CAL.events().insert(calendarId='primary',
#                 sendNotifications=True, body=EVENT2).execute()
