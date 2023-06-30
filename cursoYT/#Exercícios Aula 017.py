#Exercícios Aula 017
"""
Numa eleição existem três candidatos.
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos
de cada candidato.
"""

print("Bem vindo ao sistema eleitoral do Metaverso")
print("\nAntes de abrir as urnas para o voto, por favor informe o número total de eleitores nesta seção.")
eleitores=int(input("Digite o número total de eleitores: "))
cont=1
andre=lucio=rocha=nulo=0
print("\nNessa eleição você pode votar em três candidatos.")
print("i) Andre - 1 \nii) Lucio - 2 \niii)Rocha - 3 ")
while eleitores>=cont:
    voto=int(input("eleitor número {}, em que candidato você quer votar: ".format(cont)))
    cont+=1
    if voto==1:
        andre+=1
    elif voto==2:
        lucio+=1
    elif voto==3:
        rocha+=1
    else: 
       nulo+=1 

if nulo>0:
    print("Tivemos {} votos nulos.")
if andre>0:
    print("O candidato Andre teve {} votos.".format(andre))
if lucio>0:
    print("O candidato Lucio teve {} votos.".format(lucio))
if rocha>0:
    print("O candidato Rocha teve {} votos.".format(rocha))