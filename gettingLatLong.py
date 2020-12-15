import pandas
import googlemaps
import json
import requests

#reads the CSV file
df = pandas.read_csv('2016-2017-computer-science-report-1.csv')

#gets column called "School Name" and converts to a list
locations = df['School Name'].tolist()

# ## GOOGLE MAPS SECTION ###
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

# set up parameters for google maps api request
params = {
            'address': '',
            'key':'place your google API key here'
        }

# set up empty lists for place lat and long data
latitudes = []
longitudes = []

# Do the request and get the response data
for loc in locations:
    params['address'] = loc
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    lat = res['results'][0]['geometry']['location']['lat']
    latitudes.append(lat)
    long = res['results'][0]['geometry']['location']['lng']
    longitudes.append(long)

# add values acquired from google maps to the csv using pandas
df['latitude'] =latitudes
df['longitude'] = longitudes
df.to_csv("2016-2017-computer-science-report-1.csv", index=False)