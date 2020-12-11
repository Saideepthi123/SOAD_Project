import requests

url = "https://hotels4.p.rapidapi.com/locations/search"

querystring = {"query":"new york","locale":"en_US"}

headers = {
    'x-rapidapi-key': "5c5035c1e7msh72f101263df16acp1caccdjsna75f7e1a26e5",
    'x-rapidapi-host': "hotels4.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)


data = response.json()

citysuggestions = data['suggestions'][0]['entities']
landmarksuggestions = data['suggestions'][1]['entities']
transportsuggestions = data['suggestions'][2]['entities']
hotelsuggestions = data['suggestions'][3]['entities']

destination_ids = []
for i in range(len(citysuggestions)):
    destination_ids.append(citysuggestions[i]['destinationId'])
for i in range(len(landmarksuggestions)):
    destination_ids.append(landmarksuggestions[i]['destinationId'])
for i in range(len(transportsuggestions)):
    destination_ids.append(transportsuggestions[i]['destinationId'])
for i in range(len(hotelsuggestions)):
    destination_ids.append(hotelsuggestions[i]['destinationId'])
print(destination_ids)