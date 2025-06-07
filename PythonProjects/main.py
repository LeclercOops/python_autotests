import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0dd5b01e3a4888f685563abeab60cc15'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}

body_registration = {
    "name": "Джек",
    "photo_id": 12
}

body_changes = {
    "pokemon_id": "330580",
    "name": "Ptsh",
    "photo_id": 1
}

body_add_pokebol = {
    "pokemon_id": "330580"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body_registration)
print(response.status_code)
print(response.text)

'''response_changes = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_changes)
print(response_changes.status_code)
print(response_changes.text)'''

response_add_pokebol = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_add_pokebol)
print(response_add_pokebol.status_code)
print(response_add_pokebol.text)

message = response.json()['message']
print(message)