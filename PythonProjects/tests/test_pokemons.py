import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0dd5b01e3a4888f685563abeab60cc15'
HEADERS = {
    'Content-Type': 'application/json',
    'trainer_token': TOKEN
}
TRAINER_ID = '35227'
trainer_name = 'Ruslan' 

def test_status_code():
    response = requests.get(url= f'{URL}/trainers')
    assert response.status_code == 200

def test_my_trainer():
    response = requests.get(url= f'{URL}/trainers', params = {'trainer_id': '35227'})
    assert response.json()["data"][0]['trainer_name'] == 'Ruslan'