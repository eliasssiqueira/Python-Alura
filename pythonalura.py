
print("************************************")
print("*Bem vindo, ao jogo da adivinhação!*")
print("************************************")

numero_secreto = 80
tentativa = 3
rodada = 1

while(rodada <= tentativa):
   print("Rodada {} de {}".format(rodada, tentativa))
   chute = int (input("Digite seu palpite:"))
   print("Você digitou",chute)

   acertou = numero_secreto == chute
   maior   = chute > numero_secreto
   menor   = chute < numero_secreto

   if (acertou):
    print("Você acertou!")
   else:
      if(maior):
       print("Você errou! O seu chute é maior que o numero secreto.")
      elif(menor):
       print("Você errou! O seu chute é menor que o numero secreto.") 

   rodada = rodada + 1

print("Fim do Jogo!")  
