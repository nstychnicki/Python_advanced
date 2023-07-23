print("Bem vindo ao joguinho, tente adivinhar o número")

numero_secreto = 14

chute_str = input("Digite seu numero: ")

print("voce digitou: ", chute_str)

chute = int(chute_str)

if (numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou :(")
