from Game import Game
from Solver import Solution, dfs_solve, evaluate

def main():
	game = Game()

	while not game.is_gameover():
		game.print()
		solution: Solution = dfs_solve(game.board, game.pieces, evaluate)

		if not solution:
			break

		# Executa
		for move in solution.moves:
			print(f"\nJogando em ({move.row}, {move.col})")
			game.play(move.index, move.row, move.col)
			
	print("GAME OVER")
	game.print()

if __name__ == "__main__":
	main()
