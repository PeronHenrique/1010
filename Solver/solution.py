from Solver import Move

class Solution:
    def __init__(self, moves: list[Move], board_bits: int, evaluation: int):
        self.moves: list[Move] = moves
        self.board_bits: int = board_bits,
        self.evaluation: int = evaluation,
