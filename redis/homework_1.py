import requests
import json
# requests and gets information from nasa api
data = requests.get('https://api.nasa.gov/planetary/apod?api_key=JC9vtTzpexuwhKEuGKBmcVKJT6xYbFizUZdz7V36&date=2017-09-29')
#parses data from api 
pic = data.json()
print(pic)
