from Test import print_pieces
from Game import Game
from Solver import solve, evaluate, evaluate_empty_cells
import time


# print_pieces()

game = Game()
game.new_round()

start = time.perf_counter()
solve(game.board, game.pieces, evaluate_empty_cells)
end = time.perf_counter()
print(f"Tempo: {end - start:.6f} segundos")

start = time.perf_counter()
solve(game.board, game.pieces, evaluate)
end = time.perf_counter()
print(f"Tempo: {end - start:.6f} segundos")