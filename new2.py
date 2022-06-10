import json
from urllib import request
import requests, json

BASE_URL = "HTTPS://openweatherramp.org/data/2,5/weather?"

CITY = input("enter your city")

API_KEY = "baba45c0ccjkwnrfv489r3jkrvjk"

URL = BASE_URL +  "qa"+CITY + "sapoid" +API_KEY

response  = requests.get(URL)

if response.status_code == 200:
