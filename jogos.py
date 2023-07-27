import forca
import adivinhacao

def escolhe_jogo():
    print("Escolha o seu jogo:")
    print("1 - Adivinhação 2 - Forca")

    jogo = int(input("Selecione um: "))

    if ( jogo == 1):
        print("Jogando Adivinhação")
        adivinhacao.jogo()
    elif ( jogo == 2):
        print("Jogando Forca")
        forca.jogo()

#modularizar codigo

if (__name__ == "__main__"):
    escolhe_jogo()