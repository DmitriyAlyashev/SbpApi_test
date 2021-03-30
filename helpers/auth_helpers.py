import requests

from data.users import tk_data

url = "https://c2b.mspp.akbars.ru/identity/connect/token"

payload = {'grant_type': tk_data.get("grant_type"),
           'scope': tk_data.get("scope"),
           'client_id': tk_data.get("client_id"),
           'client_secret': tk_data.get("client_secret")}

files = [

]
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer null',
    'Cookie': 'ffa128376695be28a4a18208a2a9e635=b1bf4ce5715c740e66a276b30ff8496b'
}
session = requests.Session()
session.verify = False
response = session.post(url, headers=headers, data=payload, files=files)


print(response.text)
