from Game import Board, bits_from_string

def create_board() -> None:
	print("empty board")
	board: Board = Board(bits_from_string(""))
	board.print()
	print()

	print("not all lines defined")
	board = Board(bits_from_string("""
			XXX...XXX.
			X.X...XXX
			X.X...XXX.
			X.X...XXX.
			X.X...XXX
			XXX...XXX
			...XXX
		"""))
	board.print()
	print()

	print("more lines than SIZE")
	try:
		board = Board(bits_from_string("""
				XXX...XXX.
				X.X...XXX
				X.X...XXX.
				X.X...XXX.
				X.X...XXX
				XXX...XXX
				...XXX
				...XXX
				...XXX
				...XXX
				...XXX
			"""))
		board.print()
	except ValueError:
		print("failed with ValueError")
	print()

	print("lines larger than SIZE")
	try:
		board = Board(bits_from_string("""
				XXX...XXX.
				X.X...XXX
				X.X...XXX....
				X.X...XXX.
				X.X...XXX
				XXX...XXX
				...XXX
				...XXX
			"""))
		board.print()
	except ValueError:
		print("failed with ValueError")
	print()