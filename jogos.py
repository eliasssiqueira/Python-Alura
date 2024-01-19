import forca
import adivinhacao

print("********************")
print("**ESCOLHA SEU JOGO**")
print("********************")

print("(1) FORCA   (2) ADIVINHAÇÃO")

jogo = int(input("Qual jogo você quer jogar?"))

if(jogo == 1):
    print("Jogando forca.")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")   
    adivinhacao.jogar() 