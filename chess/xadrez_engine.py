'''
Guardará todas as informações sobre o estado do jogo, para que apareça no main.
Também determinará quais são os movimentos válidos do jogo e a memória dos movimentos.
'''

class game_state():
    def __init__(self):
        #tabuleiro é uma lista em 2d 8x8, em que cada elemento possui 2 caracteres
        #o primeiro refere-se a cor, e o segundo o tipo da peça
        self.board= [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.mover_branca=True
        self.movimento_hist= [] 
        