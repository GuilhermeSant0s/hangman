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
                
            palavra_temp = ""
            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_digitadas:
                    palavra_temp += letra_secreta
                else:
                    palavra_temp += "_"

            print(palavra_temp)

            if palavra_temp == palavra_secreta:
                print("Parabéns! Você acertou a palavra secreta!")
                break

            if tentativas == 0:
                print("Você perdeu! A palavra secreta era {}.".format(palavra_secreta))
                break

jogar_forca()

