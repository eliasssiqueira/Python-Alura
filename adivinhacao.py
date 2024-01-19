import random

def jogar():

  print("************************************")
  print("*Bem vindo, ao jogo da adivinhação!*")
  print("************************************")

  numero_secreto = random.randrange(1,101)
  tentativa = 0
  pontos = 1000

  print("Escolha o nível de dificuldade:")
  print("(1) FÁCIL  (2) MÉDIO  (3) DÍFICIL")

  nivel = int(input("Qual o nível de dificuldade?"))

  if(nivel == 1):
    tentativa = 20
  elif(nivel == 2):
    tentativa = 10
  else:
    tentativa = 5  

  for rodada in range(1,tentativa + 1):
    print("Rodada {} de {}".format(rodada, tentativa))
    chute = int (input("Digite um numero entre 1 e 100:"))
    print("Você digitou",chute)

    if(chute < 1 or chute > 100):
      print("Você deve digitar um número entre 1 e 100!")
      continue

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
      print("Você acertou! E fez {}".format(pontos))
      break

    else:
        if(maior):
         print("Você errou! O seu chute é maior que o numero secreto.")
        elif(menor):
         print("Você errou! O seu chute é menor que o numero secreto.") 
        pontos_perdidos = abs (numero_secreto - chute)
        pontos = pontos - pontos_perdidos
  print("FIM DO JOGO!")

if(__name__ == "__main__"):
  jogar()  
