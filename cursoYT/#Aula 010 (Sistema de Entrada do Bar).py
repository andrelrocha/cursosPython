#Aula 010 (Sistema de Entrada do Bar)

print("Bienvenue au salon ANDRE.\n")
print("Nous devons d'abord vous connaître mieux.\n")

nom=str(input("Quel est votre nom: "))

print("Ok,",nom,". Nous remercions.\n")

age=int(input("Quel âge avez-vous: "))

if 18<=age<60:
    print("Bienvenue,",nom, "! Vous pouvez rentrer le salon. \nProfitez!")
else:
    print("Nous sommes desolé, mais nous ne pouvons pas vous permet de rentrer.\n")
    print("Si vous pensez que c'est une erreur, rechercez l'administration.")