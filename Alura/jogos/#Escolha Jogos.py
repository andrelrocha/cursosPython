#Escolha Jogos
import adivinhação
import forca

print("Bem vindo ao Site Andre Jogos. \n\nVocê pode escolher qual jogo você quer jogar.")
print("\nNós possuímos, por enquanto, dois jogos.")
print("1) Jogo de Adivinhação. \n2) Jogo da Forca.")
choice=int(input("Escolha o jogo que você quer jogar: "))

if choice==1:
    print("\nJogando jogo de adivinhação", end="\n")
    adivinhação.jogar_adv()
elif choice==2:
    print("\nJogando jogo da forca", end="\n")
    forca.jogar_forca()
else:
    print("\nVocê não quer jogar nenhum jogo disponível.")