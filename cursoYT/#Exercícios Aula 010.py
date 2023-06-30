#Exercícios Aula 010
'''
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário o valor do saque e depois informar quantas notas de cada valor
serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na
máquina.
	Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
	notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
	Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
	três notas de 100, uma nota de 50, quatro notas de 10,
	uma nota de 5 e quatro notas de 1.
Atentar-se ao fato de que somente pode aparecer a quantidade de notas se for >0
'''

print("Seja bem-vindo ao Banco ANDRE!\n")
print("O saque limite deste caixa eletrônico é de R$ 600,00 e mínimo de R$ 10,00. \n")
print("Por favor informe o valor do seu saque. \n\nNós iremos lhe informar a quantidade de notas a serem sacadas.")

saque=int(input("Quanto você quer sacar: "))
n_100=0
n_50=0
n_10=0
n_5=0
n_1=0
falt=0
x=10<=saque<=600

if x:
    n_100=saque//100
    falt=saque%100
    if falt>0:
        n_50=falt//50
        falt=falt%50
        if falt>0:
            n_10=falt//10
            falt=falt%10
            if falt>0:
                n_5=falt//5
                falt=falt%5
                if falt>0:
                    n_1=falt//1
else:
    print("\nO valor de saque é inválido, por favor atente-se ao limite deste caixa.") 

y="notas de R$"
z="nota de R$"
a= "\nAqui está seu saque em"
q="100,00"
w="50,00"
e="10,00"
r="5,00"
t="1,00"

if x:
    if  saque&100==0: 
        print(a,n_100,y,q)
    else:
        print(a,":",sep="")
        if 1!=n_100!=0:
            print(n_100,y,q)
        if n_100==1:
            print(n_100,z,q)
        if 1!=n_50!=0:
            print(n_50,y,w)
        if n_50==1:
            print(n_50,z,w)
        if 1!=n_10!=0:
            print(n_10,y,e)
        if n_10==1:
            print(n_10,z,e)
        if 1!=n_5!=0:
            print(n_5,y,r)
        if n_5==1:
            print(n_5,z,r)
        if 1!=n_1!=0:
            print(n_1,y,t)
        if n_1==1:
            print(n_1,z,t)

print("\n\t\tVolte sempre!")