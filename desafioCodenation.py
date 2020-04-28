'''
Objetivo ...: Desafio Codenation
Autor ......: Jose Carlos
Data .......: abril/20

'''

import requests
import json
import hashlib
  

# --------------------------------------------------------------------

# Faz requisição com token e gerar arquivo json e extrai o texto cifrado

# --------------------------------------------------------------------

def escrever_json(data):
    with open('answer.json', 'w') as f:
        json.dump(data, f)


token = "f25e274340cd2439002d831f9dc6aff015a0787d"

response = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=" + token)
print (response.status_code)                      
data = response.json()

escrever_json(data)

with open('answer.json', 'r') as f:
    dados = json.load(f)
textoCifrado = dados["cifrado"] # Informação recebida: "uq nqpi cpf vjcpmu hqt cnn vjg hkuj! fqwincu cfcou"

 
# --------------------------------------------------------------------

# Decodificador para o texto gravado em textoCifrado

# --------------------------------------------------------------------

chave = 2  
tamTextoCifrado = len(textoCifrado)
textoFinal = ""

abc1 = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
abc1Recuperar = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abcIndiceNegativo = {-1:"z", -2:"y", -3:"x", -4:"w", -5:"v", -6:"u", -7:"t", -8:"s", -9:"r", -10:"q", -11:"p", -12:"o", -13:"n", -14:"m", -15:"l", -16:"k", -17:"j", -18:"i", -19:"h", -20:"g", -21:"f", -22:"e", -23:"d", -24:"c", -25:"b"}

n = 0
while n <= tamTextoCifrado:
    if n >= tamTextoCifrado:
        break
    letra = textoCifrado[n]
    valido = False
    for testeExcecao in abc1Recuperar:
        if testeExcecao == letra:
            valido = True
            break
    if valido == True:
        indiceDeLetra = abc1.get(letra)
        indice = indiceDeLetra - chave
        
        if indice >= 0:
            letraDecifrada = abc1Recuperar[indice]
            #print(letraDecifrada)
            textoFinal = textoFinal + letraDecifrada
        else:
            letraDecifrada = abcIndiceNegativo.get(indice)
            #print(letraDecifrada)
            textoFinal = textoFinal + letraDecifrada
    else:
          #print(letra) 
          textoFinal = textoFinal + letra
    n +=1
#print(textoFinal)
 
 
# --------------------------------------------------------------------

# Gera criptografica sha1 com o texto decifrado armazenado na variavel textoFinal

# --------------------------------------------------------------------


with open('answer.json', 'r') as f:
    dados = json.load(f)
textoCifrado = dados["cifrado"] # Informação recebida: "uq nqpi cpf vjcpmu hqt cnn vjg hkuj! fqwincu cfcou"

textoFinalSha1 = hashlib.sha1(textoFinal.encode('utf-8')).hexdigest()
print(textoFinalSha1)


# --------------------------------------------------------------------

# Atualiza arquivo answer.json nos campos decifrado e resumo_criptografico

# --------------------------------------------------------------------

def escrever_json(answer):
    with open('answer.json', 'w') as f:
        json.dump(conteudoJson, f)


# Armazena o conteudo do arquivo .json em momoria para alteracao e chama funcao para gerar novo arq.
with open('answer.json', 'r') as f:
    dados = json.load(f)
    conteudoJson = dados
    
conteudoJson["decifrado"] = textoFinal                  # Alterando conteudo
conteudoJson["resumo_criptografico"] = textoFinalSha1   # Alterando conteudo  
escrever_json(conteudoJson)













