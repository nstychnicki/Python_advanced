print("Bem vindo ao joguinho, tente adivinhar o número")

numero_secreto = 14
tentativas = 5


for rodada in range(1, tentativas + 1):
    print("Tentativa {} de {}".format(rodada, tentativas))
    #interpolação de strings
    chute_str = input("Digite seu numero: ")

    print("voce digitou: ", chute_str)

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou, chute um número menor!")
        elif(menor):
            print("Você errou, chute um número maior!")

print("Fim do Jogo!")