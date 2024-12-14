import requests

baseUrl = "http:localhost:5000/"

response = requests.get(
    url=baseUrl, headers={"Content-Type": "application/json"}, data=None
)

if response.status_code == 200:
    response = response.json()
    print(response)
