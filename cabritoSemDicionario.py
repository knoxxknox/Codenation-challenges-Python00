# Decodificador knoxxknox


textoFinal = ""
textoCifrado = "a"
chave = 1
tamTextoCifrado = len(textoCifrado)


cabrito = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

n = 0
while n <= tamTextoCifrado:
    if n >= tamTextoCifrado:
        break
    letra = textoCifrado[n]
    valido = False
    for testeExcecao in cabrito: 
        if testeExcecao == letra:
            valido = True
            break
    if valido == True:
        indiceDeLetra = cabrito.index(letra)
        indice = indiceDeLetra - chave
        if indice >= 0:
            letraDecifrada = cabrito[indice]
            textoFinal = textoFinal + letraDecifrada
        else:
            
            cabritoInvertido = cabrito[::-1] 
            # cabritoInvertido é uma lista invertida de cabrito [z, y, w,...] vocë também pode criar manualmente, no momento em que criar cabrito
            # como no python posso usar esse recurso, não preciso escrever na mão o alfabeto de trás para frente
            # basta multiplicar o indice (que é negativo) por -1, para remover o negativo, assim por exemplo, o valor -2, será 2 que nesta lista (cabritoInvertido) o indice 2 é o y.
            
            indice = (indice * -1)
            
            letraDecifrada = cabritoInvertido[indice]
            textoFinal = textoFinal + letraDecifrada
    else:
          #print(letra) 
          textoFinal = textoFinal + letra
    n +=1
print(textoFinal)
       
