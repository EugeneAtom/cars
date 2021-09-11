import json
import urllib
import requests

where = urllib.parse.quote_plus("""
{
    "Year": {
        "$gt": 2009
    }
}
""")
url = 'https://parseapi.back4app.com/classes/Carmodels_Car_Model_List?limit=5000&order=Year&where=%s' % where
headers = {
    'X-Parse-Application-Id': 'QjX6zUIOEAQJ4bjYFmdIxKrCF6FOWUY9TVnKxj0h',  # This is your app's application id
    'X-Parse-REST-API-Key': 'KZ8re1wY0gNgYH3NKvwyrPyRKU3KGB1AelfV7P1P'  # This is your app's REST API key
}
data = json.loads(requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
# print(json.dumps(data, indent=2))
print(len(data["results"]))

with open("car_data.json", "w+") as file:
    file.write(json.dumps(data))


