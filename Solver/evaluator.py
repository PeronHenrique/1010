from Game import Board, SIZE

#TODO: posições possiveis para as maiores peças
def evaluate(board: Board) -> float:
    empty_cells = board.empty_cells()
    filled_regions = regions(board, False)
    empty_regions = regions(board, True)
    near_lines = count_near_complete_lines(board)

    count_regions_empty = len(empty_regions)
    largest_region_empty = max([size for size, _ in empty_regions])
    count_regions_filled = len(filled_regions)
    largest_region_filled = max([size for size, _ in filled_regions])
    perimeter = sum([perimeter for _, perimeter in filled_regions])

    isolated = sum([1 if size == 1 else 0 for size, _ in empty_regions])
    holes = sum([1 if size <= 3 else 0 for size, _ in empty_regions])

    #TODO: calculate score based on filled regions

    evaluation = (
        + empty_cells * 2
        + largest_region_empty * 1.5
        + largest_region_filled * 1.5
        + near_lines * 2
        - perimeter
        - holes * 5
        - isolated * 5
        - count_regions_empty * 10 
        - count_regions_filled * 5
    )

    return evaluation

# Conta linhas e colunas com SIZE - 2 ou SIZE - 1 preenchido
# SIZE - 2 ganha 1 ponto
# SIZE - 1 ganha 2 pontos
def count_near_complete_lines(board: Board) -> int:
    count = 0

    for row in range(SIZE):
        filled = 0
        for col in range(SIZE):
            position = row * SIZE + col
            if board.bits & (1 << position):
                filled += 1

        if filled >= SIZE - 2:
            count += filled - SIZE - 3

    for col in range(SIZE):
        filled = 0
        for row in range(SIZE):
            position = row * SIZE + col
            if board.bits & (1 << position):
                filled += 1
                
        if filled >= SIZE - 2:
            count += filled - SIZE - 3

    return count

# Calcula o tamanho de uma região ortogonalmente conectada
# retorna a área e perimetro, não se preocupa com formato
# empty = False calcula área preenchida
# empty = True calcula área vazia
def flood_fill(board: Board, start_row: int, start_col: int, visited: set, empty: bool) -> tuple[int, int]:
    stack = [(start_row, start_col)]
    size = 0
    perimeter = 0

    while stack:
        row, col = stack.pop()

        if row < 0 or row >= SIZE:
            continue
        if col < 0 or col >= SIZE:
            continue
        if (row, col) in visited:
            continue

        if empty ^ board.is_empty(row, col):
            perimeter += 1
            continue

        visited.add((row, col))
        size += 1

        stack.append((row - 1, col))
        stack.append((row + 1, col))
        stack.append((row, col - 1))
        stack.append((row, col + 1))

    return size, perimeter

#Retorna lista com (size, perimeter) das regiões ortogonalmente conectadas
# empty = False regiões preenchidas
# empty = True regiões vazias
def regions(board: Board, empty: bool) -> int:
    visited = set()
    regions = []

    for row in range(SIZE):
        for col in range(SIZE):
            regions.append(flood_fill(board, row, col, visited, empty))

    return regions

