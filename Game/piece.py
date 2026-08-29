from Game import SIZE

class Piece:
    def __init__(self, name: str, cells: list[tuple[int, int]]):
        self.name: str = name

        # Dimensões da peça
        self.width: int = max(col for _, col in cells) + 1
        self.height: int = max(row for row, _ in cells) + 1

        # Converte cells para bitboard SIZExSIZE
        self.mask: int = 0

        for row, col in cells:
            position = row * SIZE + col
            self.mask |= 1 << position

    def print(self) -> None:
        for row in range(self.height):
            line = []
            for col in range(self.width):
                line.append(
                    "X" if bool(self.mask & (1 << (row * SIZE + col))) else "."
                )

            print(" ".join(line))