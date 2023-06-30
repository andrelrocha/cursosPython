#Exercícios Aula 015
"""
Dizemos que um inteiro positivo n é perfeito se for igual à soma de
seus divisores positivos diferentes de n.

Exemplo: 6 é perfeito, pois 1+2+3 = 6.
       Dado um inteiro positivo n, verificar se n é perfeito.
"""

n = int(input("Digite n: "))
cont, soma = 2, 1
while cont<n:
    if n%cont==0:
        soma+=cont
    cont+=1
if soma==n:
    print("O número",n,"é perfeito")
else:
    print("O número",n,"não é perfeito")

"""
Dados n e uma seqüência de n números inteiros,
determinar a soma dos números pares.
"""

num_esc=int(input("Escolha o n para determinar a soma dos números pares: "))
num_esc*=2
cont=2
while cont<=num_esc:
    print(cont)
    soma=cont
    cont+=2
    soma=soma+cont
print("O valor final da soma de todos os n números pares é",soma)