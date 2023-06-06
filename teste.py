import requests


dado = requests.post('http://127.0.0.1:8000/solar_painel/send/428/15000000000000000000')
print(dado.json())
