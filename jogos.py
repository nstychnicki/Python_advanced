import forca
import adivinhacao

print("Escolha o seu jogo:")
print("1 - Adivinhação \n 2 - Forca")

jogo = int(input("Selecione um: "))

if ( jogo == 1):
    print("Jogando Adivinhação")
    forca.jogo()
elif ( jogo == 2):
    print("Jogando Forca")
    adivinhacao.jogo()

#modularizar codigo