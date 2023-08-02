import random


def jogo():
    mensagem_boasvindas()
    palavra_secreta = palavra_aleatoria()
    letras_certas = inicializa_palavras(palavra_secreta)
    # passa o parametro para que a função acesse a palavra_secreta
    print(letras_certas)

    enforcou = False
    acertou = False
    # precisa de letra maiuscula para definir booleano
    tentativa = 0

    while (not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            chute_correto(chute, letras_certas, palavra_secreta)
        else:
            tentativa += 1
            print("Restam {} tentativas".format(6 - tentativa))

        enforcou = tentativa == 6
        # quando houver 6 tentativas o enforcou sera True
        acertou = "_" not in letras_certas
        # faz com que o programa pare quando não houver mais _
        print(letras_certas)

    if (acertou):
        mensagem_ganhador()
    else:
        mensagem_perdedor()


def mensagem_boasvindas():
    print("Bem vindo ao joguinho!")


def palavra_aleatoria():
    arquivo = open("palavras.txt", "r", encoding="utf8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    # randomiza dentro do range do arquivo txt
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_palavras(palavra):
    return ["_" for letra in palavra]
    # [] serve para criar listas


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    # entrada do usuario - string types
    # strip - tira os espaços/ upper - deixa tudo em caps
    # não alteram a string original (string sao imutaveis)
    return chute


def chute_correto(chute, letras_certas, palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas[posicao] = letra
            # substitui a letra certa dentro da lista
        posicao += 1


def mensagem_ganhador():
    print("Você ganhou!")


def mensagem_perdedor():
    print("Você perdeu :(")


if (__name__ == "__main__"):
    jogo()