def parOuImpar(numero:float) -> str:
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
def positivoNegativoNeutro(numero:float) -> str:
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Neutro"
    

def maiorNumero(lista_de_numeros:list) -> float:
    maior = lista_de_numeros[0]
    for numero_da_vez in lista_de_numeros:
        if numero_da_vez > maior:
            maior = numero_da_vez
    return maior

def menorNumero(lista_de_numeros:list) -> float:
    menor = lista_de_numeros[0]
    for numero_da_vez in lista_de_numeros:
        if numero_da_vez < menor:
            menor = numero_da_vez
    return menor

def mediaDosNumeros(lista_de_numeros:list) -> float:
    soma_total = 0
    for numero_da_vez in lista_de_numeros:
        soma_total += numero_da_vez
    media = soma_total / len(lista_de_numeros)
    return media