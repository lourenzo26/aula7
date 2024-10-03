def contaVogais(palavra:str) -> int:
    contador = 0
    vogais = "aeiouáàâãéêèíóôõú"
    for letra_da_vez in palavra:
        if letra_da_vez.lower() in vogais:
            contador += 1
    return contador

def contaConsoantes(palavra:str) -> int:
    contador = 0
    consoantes = "bcdfghjklmnpqrstvxywzç"
    for letra_da_vez in palavra:
        if letra_da_vez.lower() in consoantes:
            contador += 1
    return contador

def contarPalavras(frase:str) -> int:
    contador = 1
    for caracter_da_vez in frase:
        if caracter_da_vez == " ":
            contador += 1
    return contador


def transformarMaiusculo(palavra:str) -> str:
    return palavra.upper()


def transformarMinusculo(palavra:str) -> str:
    return palavra.lower()