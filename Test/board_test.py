from Game import Board, bits_from_string

def create_board() -> None:
	board: Board = Board(bits_from_string("""
			XXX...XXX.
			X.X...XXX.
			X.X...XXX.
			X.X...XXX.
			X.X...XXX.
			XXX...XXX.
			...XXX
		"""))
	
	board.print()