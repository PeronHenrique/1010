from itertools import permutations

from Game import Board
from Solver import Move, Solution, evaluate

# TODO: memoization

class Solver:
    def solve(self, board: Board, pieces: list[int]) -> Solution:
        best_solution: Solution = None

        for ordered_pieces in permutations(pieces):
            candidate: Solution = _dfs(board=board.copy(), indicies=ordered_pieces)

            # Uma ordem pode não permitir jogar todas as peças
            if candidate is None:
                continue

            if (best_solution is None or candidate.evaluation > best_solution.evaluation):
                best_solution = candidate
        
        return best_solution
    


def _dfs(board: Board, indicies: list[int],
        index: int =0, moves: list[Move] = []) -> Solution:

    if index == len(indicies):
        evaluation = evaluate(board)
        moves_copy = moves.copy()
        return Solution(moves=moves_copy, board_bits=board.bits, evaluation=evaluation)

    best_solution: Solution = None

    for row, col in board.get_valid_positions(indicies[index]):
        new_board: Board = board.copy()
        new_board.place(indicies[index], row, col)

        move = Move(index=indicies[index], row=row, col=col)
        moves.append(move)

        result: Solution = _dfs(
            board = new_board,
            indicies=indicies,
            index=index + 1,
            moves=moves,
        )

        moves.pop()

        if result is None:
            continue

        if (best_solution is None or result.evaluation > best_solution.evaluation):
            best_solution = result

    return best_solution

    

