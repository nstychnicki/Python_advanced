def jogo():
    print("Bem vindo ao joguinho!")

    palavra_secreta = "nataly"
    letras_certas = ["_","_","_","_","_","_"]
    #[] serve para criar listas

    print(letras_certas)
    
    enforcou = False
    acertou = False
    #precisa de letra maiuscula para definir booleano

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()
        # entrada do usuario - string types
        #não alteram a string original (string sao imutaveis)

        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_certas[posicao] = letra
                #substitui a letra certa dentro da lista
            posicao = posicao + 1
        print(letras_certas)
    print("Fim do Jogo!")

if (__name__ == "__main__"):
    jogo()

