import requests
import re
import time
import json
from bs4 import BeautifulSoup
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
    print(dict['name'])
    print(name)
    print(date)
    print(time)
    print(location)
    print(' ')

    # for i in range(len(info)-2):
    #     em = info[i]
    #     list_names.append(em)=[]
    #     list_dates=[]
    #     list_locations=[]
    #     list_info=[]
    #     print(em.text)

# with open("myExcitingNewFile.json", "w+") as f:
#     f.write("TEST")
#
# # stuff
scopes = ['https://www.googleapis.com/auth/calendar']
#
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_console()

# pickle.dump(credentials, open("token.pkl", "wb"))
# credentials = pickle.load(open("token.pkl", "rb"))
#
# service = build('calendar', 'v3', credentials=credentials)
#
# result = service.calendarList().list().execute()

# response = requests.post(
#     url='https://www.googleapis.com/calendar/v3/calendars/CALENDAR_ID/events/quickAdd',
#     data={
#         'text': 'EVENT_TEXT',
#     },
#     headers={
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Authorization': '4/twHd14I71OG_N-lijL5HJ9BdcjFgPW9jjVdho4LeqnbzZI_X3sZ52m0S3ZqlEOFcxBmfyzhOjkxWWJfFrSYw8Fc',
#     },
# )
# response.raise_for_status()
# print(response.json())
