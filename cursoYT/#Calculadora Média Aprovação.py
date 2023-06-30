#Calculadora Média Aprovação
sum1=float(input("Qual foi sua nota no primeiro bimestre: "))
sum2=float(input("Qual foi sua nota no segundo bimestre: "))
sum3=float(input("Qual foi sua nota no terceiro bimestre: "))
sum4=float(input("Qual foi sua nota no quarto bimestre: "))
x=(sum1+sum2+sum3+sum4)/4
aprovação=x>=7
mérito=x>=9.5
if aprovação:
    print("Parabéns você foi aprovado")
    print("Sua nota foi",x)
    if mérito:
        print("Passe na coordenação para buscar sua medalha.")
else:
    print("Procure a coordenação")