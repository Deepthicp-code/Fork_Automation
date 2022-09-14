import requests

URL = "https://pokeapi.co/api/v2/pokemon?limit=30"

resp = requests.get("https://pokeapi.co/api/v2/pokemon?limit=30")
assert (resp.status_code == 200), "Status code is not 200:" +\
    str(resp.status_code)
print("status_code="+str(resp.status_code))
files = resp.json()
print(files)

resp = requests.get("https://pokeapi.co/api/v2/berry/1/")
assert (resp.status_code == 200), "Status code is not 200:" +\
    str(resp.status_code)
print("status_code="+str(resp.status_code))
print(resp.headers)
print(resp.json)
print(resp.content)
