#Jogo de Forca
def jogar_forca():

    print("Olá visitante. Que tal jogar um jogo?")
    print("\nChute um número dentro do limite previsto (1-100) e veja se você acerta o número secreto.")
    print("\nNo nosso jogo temos três níveis de dificuldades:")
    print("1) Fácil \n2) Médio \n3) Difícil")
    print("\nDigite um número entre 1 e 3 para definir o nível do seu jogo.")
    nivel=int(input("Digite o nível de dificuldade que você quer jogar: "))
    tentativas=0
    pontos=1000
    cont=0

    print("\nFim do Jogo. \n\nVolte Novamente!")
#Se você executa o arquivo forca como main, execute
if(__name__=="__main__"):
    jogar_forca()
'''
Quando rodamos diretamente um arquivo no Python, 
ele internamente cria uma variável e a preenche. 
E através dessa variável podemos fazer uma consulta, 
pois se ela estiver preenchida, significa que o arquivo foi executado diretamente, 
mas se a variável não estiver preenchida, então significa que o arquivo só foi importado.

Essa variável é a __name__, e ela é preenchida com o valor __main__ 
caso o arquivo seja executado diretamente.
'''