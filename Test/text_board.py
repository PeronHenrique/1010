from Game import Board, SIZE

def board_from_string(board_str: str) -> Board:
    lines = [
        line.strip()
        for line in board_str.strip().splitlines()
        if line.strip()
    ]

    if any(len(line.split()) > SIZE for line in lines):
        raise ValueError("Board invalido")

    bits = 0

    for row, line in enumerate(lines):
        for col, cell in enumerate(line.split()):
            if cell == "X":
                bits |= 1 << (row * SIZE + col)
            elif cell != ".":
                raise ValueError(f"Célula inválida: {cell}")

    return Board(bits)