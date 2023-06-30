#Exercícios Aula 011
"""
Faça um Programa que leia um número inteiro menor que 1000 e
imprima a quantidade de centenas, dezenas e unidades do mesmo.
	Observando os termos no plural a colocação do "e", da vírgula
	entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301,
	101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
print("Bem vindo ao programa ANDRE!")
print("\nPor favor digite um número e nós iremos apresentar a qtd de centenas, dezenas e centenas.")
print("\nO número digitado deve ser inteiro e menor que 1000.")
x=int(input("Digite um número: "))
resto=x%100
centena=x//100
dezena=resto//10
unidade=resto%10

print("\nPara o número digitado, temos: ",end="")

if x<1000:
    if resto==0:
        if centena>1:
            print(centena,"centenas.")
        elif centena==1:
            print(centena,"centena.")
    elif resto%10==0:
        if centena>1:
                print(centena,"centenas e ",end="")
        else:
                print(centena,"centena e ",end="")    
        if dezena>1:
            print(dezena,"dezenas.")
        elif dezena==1:
            print(dezena,"dezena.")
    else:
        if centena==0:
            print("")
        elif centena>1:
            print(centena,"centenas, ",end="")
        else:
            print(centena,"centena, ",end="") 
        if dezena==0:
            print("")
        elif dezena>1:
            print(dezena,"dezenas",end="")
        else:
            print(dezena,"dezena",end="")   
        if unidade>1:
            print(" e",unidade,"unidades.")
        elif unidade==1:
            print(" e",unidade,"unidade.")
else:
    print("Por favor digite um número válido.")

"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
print("Bem vindo ao programa dos extremos \n\nNós iremos lhe mostrar o maior e o menor número digitado.")
sum1=int(input("informe seu primeiro número: "))
sum2=int(input("informe seu segundo número: "))
sum3=int(input("informe seu terceiro número: "))

if sum1!=sum2!=sum3:
    if sum1>sum2>=sum3:
        print(sum1,sum3)
    elif sum1>sum3>=sum2:
        print(sum1,sum2)
    elif sum2>sum1>=sum3:
        print(sum2,sum3)
    elif sum2>sum3>=sum1:
        print(sum2,sum1)
    elif sum3>sum2>=sum1:
        print(sum3,sum1)
    elif sum3>sum1>=sum2:
        print(sum3,sum2)
else: 
    print("você digitou três números iguais")