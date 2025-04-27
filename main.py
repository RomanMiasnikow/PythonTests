import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '91b417f8cb0467e4a077eee6598d468d'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "romanmiasnikow93@yandex.ru",
    "password": "CharlamowWB48_81"
}
body_confirmation = {
    "trainer_token": TOKEN 
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": -1
}


'''response = requests.post(url = f'{URL}trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

id = response_create.json()['id']
print(id)


body_create = {
    "pokemon_id": id,
    "name": "Хагги Вагги",
    "photo_id": 2
}

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

{
    "pokemon_id": id
}

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_create)
print(response_create.text)