import requests

API_KEY = "API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_stores():
    url = "https://api.printify.com/v1/shops.json"
    response = requests.get(url, headers=headers)
    return response.json()

stores = get_stores()

for store in stores:
    print(f"Store Name: {store['title']}, Store ID: {store['id']}")
