#Exercícios Aula 013
"""
Dado um número inteiro positivo n,
calcular a soma dos n primeiros números inteiros positivos.
"""
n=int(input("Digite um número: "))
soma=n
razao=n-1

while razao>0:
    soma=soma+razao
    razao-=1
print(soma)

"""
Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares.
n = 4 --> 1, 3, 5, 7
n = 3 --> 1, 3, 5
n = 7 --> 1, 3, 5, 7, 9, 11, 13
"""

n=int(input("Digite um número inteiro positivo representativo que você queira descobrir os números ímpares: "))
sum1=1
cont=0

print("n =",n, "--> ",end="")
while cont<n:
    print(sum1,end=". ")
    sum1+=2
    cont+=1