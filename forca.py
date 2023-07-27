def jogo():
    print("Bem vindo ao joguinho!")

    palavra_secreta = "nataly"

    enforcou = False
    acertou = False
    #precisa de letra maiuscula para definir booleano

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        # entrada do usuario - string types

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, posicao + 1))
            posicao = posicao + 1

    print("Fim do Jogo!")

if (__name__ == "__main__"):
    jogo()

