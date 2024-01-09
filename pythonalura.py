print("***********************************")
print("Bem vindo, ao jogo da adivinhação!")
print("***********************************")

numero_secreto = 80


chute = int (input("Digite seu palpite:"))


print("Você digitou",chute)

if (numero_secreto == chute):
    print("Você acertou!")
else: print("Você errou!")





