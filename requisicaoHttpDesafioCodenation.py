# Faz requisição com token e gerar arquivo json

import requests
import json
  
def escrever_json(lista):
    with open('desafioCodenation.json', 'w') as f:
        json.dump(lista, f)

'''
def carregar_json(arquivo):
    with open('desafioCodenation.json', 'r') as f:
        return json.load(f)
'''

token = "f25e274340cd2439002d831f9dc6aff015a0787d"

response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=" + token)
print (response.status_code)                      
data = response.json()

escrever_json(data)
