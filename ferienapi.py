#!/usr/bin/env python

#Danke an
#ferien-api
#https://blog.smartnoob.de/2014/04/15/ferien-feiertag-api-fuer-deutschland/


import requests
import json
import datetime
response = requests.get("http://api.smartnoob.de/ferien/v1/ferien/?bundesland=he")
print(response.status_code)
data = json.loads(response.text)
for element in data['daten']:
    start = datetime.datetime.fromtimestamp(element['beginn'])
    ende = datetime.datetime.fromtimestamp(element['ende'])
    print element['title'] , " " , start.strftime('%Y-%m-%d') , " " , ende.strftime('%Y-%m-%d')

