import random


def jogo():
    print("Bem vindo ao joguinho!")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    #randomiza dentro do range do arquivo txt
    palavra_secreta = palavras[numero].upper()

    letras_certas = ["_" for letra in palavra_secreta]
    #[] serve para criar listas
    tentativa = 0

    print(letras_certas)
    
    enforcou = False
    acertou = False
    #precisa de letra maiuscula para definir booleano

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        # entrada do usuario - string types
        #strip - tira os espaços/ upper - deixa tudo em caps
        #não alteram a string original (string sao imutaveis)

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_certas[posicao] = letra
                    #substitui a letra certa dentro da lista
                posicao += 1

        else:
            tentativa += 1
            print("Restam {} tentativas" .format(6 - tentativa))

        enforcou = tentativa == 6
        #quando houver 6 tentativas o enforcou sera True
        acertou = "_" not in letras_certas
        #faz com que o programa pare quando não houver mais _
        print(letras_certas)

    if(acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu :(")
    print("Fim do Jogo.")

if (__name__ == "__main__"):
    jogo()

