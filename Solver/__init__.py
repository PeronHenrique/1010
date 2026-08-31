from .move import Move
from .solution import Solution
from .evaluator import evaluate, evaluate_empty_cells, count_near_complete_lines, flood_fill, get_regions
from .solver import solve


#TODO: 
# criar uma função de avaliação com varios calculos
# posições que pode por cada peça
# buracos
# regiões vazias etc
# ela aceita uma lista de pesos
# e usa para calcular o fitnes dos tabuleiros
# 
# usa Algoritmo Genetico com os pesos como DNA, e pontuação no jogo como fitnes