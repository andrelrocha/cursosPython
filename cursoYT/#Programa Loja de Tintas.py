#Programa Loja de Tintas
'''
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''
area=int(input("Qual a área a ser pintada: "))
#cria-se a razão através do meu input, atentando-se a possibilidade de restos
litros=area//3
if area%3>0:
    litros=litros+1
latas=litros//18
if litros&18>0:
    latas=latas+1
print("Você irá precisar de",latas,"latas.")
print("O valor final será de",latas*80, "Reais")