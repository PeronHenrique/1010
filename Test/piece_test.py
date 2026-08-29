from Game import PIECES

def print_pieces() -> None:
	for piece in PIECES:
		print(f"\n {piece.name}:")
		piece.print()
		