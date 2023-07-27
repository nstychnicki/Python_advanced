import random
#biblioteca
def jogo():
    print("Bem vindo ao joguinho, tente adivinhar o número")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 100

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 20adivinhacao.py
    elif (nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        #interpolação de strings

        chute_str = input("Digite seu numero: ")
        print("voce digitou: ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Digite apenas números entre 1 e 100")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou! Você fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou, chute um número menor!")
            elif(menor):
                print("Você errou, chute um número maior!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!")