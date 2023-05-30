import random

def jogar_forca():
    palavras = ["casa", "carro", "pessoa", "computador", "python", "programacao"]
    palavra_secreta = random.choice(palavras)
    letras_digitadas = []
    tentativas = 6

    while True:
        letra = input("Digite uma letra: ")

        if letra in letras_digitadas:
            print("Você já digitou essa letra. Tente outra.")
        else:
            letras_digitadas.append(letra)

            if letra in palavra_secreta:
                print("Você acertou uma letra!")
            else:
                tentativas -= 1
                print("Você errou uma letra. Você tem {} tentativas.".format(tentativas))
