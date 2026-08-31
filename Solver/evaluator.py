from Game import Board, SIZE, PIECES
def evaluate_empty_cells(board: Board) -> float:
    return board.empty_cells()

def evaluate(board: Board) -> float:
    filled_regions = get_regions(board, False)
    empty_regions = get_regions(board, True)

    near_lines_points = count_near_complete_lines(board)
    empty_cells = board.empty_cells()
    count_regions_empty = len(empty_regions)
    largest_region_empty = max([size for size, _ in empty_regions])
    count_regions_filled = len(filled_regions)
    largest_region_filled = max([size for size, _ in filled_regions])
    perimeter = sum([perimeter for _, perimeter in filled_regions])
    isolated = sum([1 if size == 1 else 0 for size, _ in empty_regions])
    holes = sum([1 if size <= 3 else 0 for size, _ in empty_regions])

    positions = [len(board.get_valid_positions(piece_index)) for piece_index in range(len(PIECES))]

    #TODO: calculate score based on filled regions and position count

    evaluation =  empty_cells * 2 
    + largest_region_empty * 1.5 
    + largest_region_filled * 1.5  
    + near_lines_points * 2 
    - perimeter
    - holes * 5 
    - isolated * 5 
    - count_regions_empty * 10  
    - count_regions_filled * 5
    
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
            count += filled - (SIZE - 3)

    for col in range(SIZE):
        filled = 0
        for row in range(SIZE):
            position = row * SIZE + col
            if board.bits & (1 << position):
                filled += 1
                
        if filled >= SIZE - 2:
            count += filled - (SIZE - 3)

    return count

# Calcula o tamanho de uma região ortogonalmente conectada
# retorna a área e perimetro, não se preocupa com formato
# empty = False calcula área preenchida
# empty = True calcula área vazia
def flood_fill(board: Board, start_row: int, start_col: int, visited: set, empty: bool) -> tuple[int, int]:
    stack = [(start_row, start_col)]
    size = 0
    perimeter = 0
    entry = True

    while stack:
        row, col = stack.pop()

        if row < 0 or row >= SIZE:
            continue
        if col < 0 or col >= SIZE:
            continue
        if (row, col) in visited:
            continue

        if empty ^ board.is_empty(row, col):
            if entry:
                entry = False
            else:
                perimeter += 1
            continue

        visited.add((row, col))
        size += 1
        entry = False

        stack.append((row - 1, col))
        stack.append((row + 1, col))
        stack.append((row, col - 1))
        stack.append((row, col + 1))

    return size, perimeter

#Retorna lista com (size, perimeter) das regiões ortogonalmente conectadas
# empty = False regiões preenchidas
# empty = True regiões vazias
def get_regions(board: Board, empty: bool) -> int:
    visited = set()
    regions = []

    for row in range(SIZE):
        for col in range(SIZE):
            region = flood_fill(board, row, col, visited, empty)    
            if region != (0, 0):
                regions.append(region)

    return regions