#Exercícios Aula 009
'''
Faça um Programa que peça um valor e mostre na tela
se o valor é positivo ou negativo.
'''

sum1=float(input("Digite um número:"))
print("Será se o número é positivo ou negativo?")
if sum1>0:
    print("O número",sum1,"é positivo")
if sum1<0:
    print("O número",sum1,"é negativo")
if sum1==0:
    print("O número 0 é neutro")

'''
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 4 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias
'''

print("Bem-vindo à loja de tintas ANDRÉ TINTAS.\n")
print("Aqui nós vendemos:\nLatas de tinta de 18 litros, por R$ 80,00.\nGalões de tinta de 4 litros, por R$ 25,00.")
area=int(input("Digite a quantidade de m² da área a ser pintada: "))
area=area*1.1
print("\nPor preucação, recomendamos que você compre tinta o suficiente para a área de", area, "m² com 10% de margem.")

tinta=area//6
if tinta%6>0:
    tinta=tinta+1
print("\nPara a área desejada, será necessário, com margem, a quantidade de",tinta,"litros de tinta")

lata=tinta//18
if tinta%18>0:
    lata=lata+1
valor1=lata*80
print("\nPara concluirmos seu pedido em latas de 18 litros, o valor final é de",valor1,"reais")

galao=tinta//4
if tinta%4>0:
    galao=galao+1
valor2=galao*25
print("\nPara concluirmos seu pedido em galões de 4 litros, o valor final é de",valor2,"reais")

#Em geral comprar lata é melhor, com exceção aos restos inferiores ou iguais à 12, que compra 3 galões
lata=tinta//18
galao=0
litros_restantes=tinta%18
if litros_restantes<=12:
    galao=litros_restantes//4
    if litros_restantes%4>0:
        galao+=1
else: lata+=1
valor3=galao*25+lata*80

print("\nCaso escolha uma maior economia ",end="")
if lata==1:
    print("você precisará comprar",lata,"lata de tinta ", end="")
else:
    print("você precisará comprar",lata,"latas de tinta ", end="")
if galao==1:
    print("e",galao,"galão de tinta.")
if galao>1:
    print("e",galao,"galões de tinta.")
if galao==0:
    print("")

print("O valor final da combinação é de", valor3,"reais")