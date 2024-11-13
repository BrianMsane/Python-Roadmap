<h1>Body and Header</h1>

Headers provide meta-data information about the request and they typically include:
<ul>
    <li>Content-Type: specifies the format of the request/response body</li>
    <li>Authorization: provides credentials for authenticating the client</li>
    <li>User-Agent: provides information tabout the software making the request</li>
</ul>
It is important to note that you can alway add new, customer, headers to your headers for as long as you need then.

Bodies contain the actual data being sent to teh server, for instance, when making a post request, the body might contain tthe details of the new resource to be created. Each request or response body differs according to the 


```python
import os
import requests
import dotenv
dotenv.load_dotenv()

url = 'http:localhost:3000/app' # URL with a prefix
token = os.getenv('TOKEN')
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}
body = {
    'name': 'Brian',
    'age': '77',
    'gender': 'Male'
}
response = request.post(url, headers=headers, body=body)
if response.status_code == 200:
    return response.json()
```

By clearly defining the headers and bodies in your API requests, you ensure taht your communication with teh server are properly formatted and secure.