import openrouteservice as ors
from openrouteservice import convert
from config import API_KEY #Create config file
import json
import requests


coords = ((8.34234,48.23424),(8.34423,48.26424), (8.34523,48.24424), (8.41423,48.21424))

client = ors.Client(key=API_KEY) # Specify your personal API key

print(
    ors.geocode.pelias_search(client,"6217 Greenleaf Ave, Whittier, CA 90601",country="US")["features"][0]["geometry"]
)
'''
pelias = ors.geocode.pelias_reverse(client,(8.34234,48.23424),size=1)
routes = client.directions(coords, profile='cycling-regular', optimize_waypoints=True)
geometry = convert.decode_polyline(routes['routes'][0]['geometry'])

print(json.dumps(pelias, indent = 1))
print(json.dumps(routes,indent = 1))
print(geometry)
'''