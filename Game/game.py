import random

from Game import Piece, Board, PIECES, SIZE, N_PIECES


class Game:
    board : Board
    score : int
    pieces : list[int]

    def __init__(self):
        self.board = Board()
        self.score = 0
        self.pieces = []

    def new_round(self) -> list[int]:
        if len(self.pieces) > 0:
            return self.pieces
        
        self.pieces = random.choices(range(len(PIECES)), k=N_PIECES)
        return self.pieces

    def play(self, piece_index: int, row: int, col: int) -> Board:
        piece: Piece = PIECES[piece_index]
        rows, cols = self.board.place(piece_index, row, col)

        points: int = piece.mask.bit_count()
        cleared: int = len(rows) + len(cols)
        points += cleared * (cleared + 1) * SIZE / 2

        self.score += points

        self.pieces.remove(piece_index)
        return self.board
        

    def print(self) -> None:
        print(f"\nPontuação: {self.score}")
        print("\nTABULEIRO")
        self.board.print()
        print("\nPEÇAS:")
        for index in self.pieces:
            PIECES[index].print()
            print()

    def is_gameover(self) -> bool:
        if len(self.pieces) == 0:
            self.new_round()

        for index in self.pieces:
            if len(self.board.get_valid_positions(index=index)) > 0:
                return False

        return True
