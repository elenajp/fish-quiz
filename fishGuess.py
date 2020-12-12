import requests
import json

url = "https://fishbase.ropensci.org/species"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
fish_data = json.loads(response.text)
fish_species = fish_data['data'][0]['Species']
dangerous = fish_data['data'][0]['Dangerous']
comments = fish_data['data'][0]['Comments']
image = fish_data['data'][0]['image']
print(fish_data['data'][0]['image'])
