import random

def jogar_forca():
    palavras = ["casa", "carro", "pessoa", "computador", "python", "programacao"]
    palavra_secreta = random.choice(palavras)
    letras_digitadas = []
    tentativas = 6
