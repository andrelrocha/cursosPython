'''
Main driver file. 
Cuidará do input e rodará o jogo para o usuário
'''

'''
import pygame 
import chess.xadrez_engine.game_state()
from chess import xadrez_engine.py
'''

WIDTH=HEIGHT=400
DIMENSION=8
TAMANHO_QUAD=HEIGHT//DIMENSION
MAX_FPS=15
IMAGES={}

'''
inicializa um dicionário global de imagens.
'''
def carregar_imgs():
    pecas=["wp","wR","wN","wB","wQ","wK","wB","wN","wR","bp","bR","bN","bB","bQ","bK","bB","bN","bR"]
    for piece in pecas:
        IMAGENS[piece]=p.pecas.load("pecas/" + piece + ".png")