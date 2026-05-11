from pyscript import web, fetch, display
import requests

url = f"https://pokeapi.co/api/v2/pokemon/pikachu"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['name']}")
    print(f"Height: {data['height']}")
    print(f"Abilities: {[ability['ability']['name'] for ability in data['abilities']]}")

# This is how you change the text of an item
new_text = "Yes Boys"
header_access = web.page["main_header"]
header_access.innerText = new_text

client = pokepy.V2Client()
print(client.get_pokemon(14))

