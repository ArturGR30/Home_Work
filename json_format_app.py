name = input("enter domain name or ip address: ")
address = f"http://ip-api.com/json/{name}"

import requests

response = requests.get(address)

data = response.json()

if data["status"] == "success":
    print("region", data["regionName"])
    print("organization", data["org"])
else:
    print("ERROR. Information for this domain is not exist")

