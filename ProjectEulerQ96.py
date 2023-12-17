def extractGrids():
    grids = []
    fileName = 'sudoku.txt'

    with open(fileName, 'r') as file:
        for i in range(50):
            currentGrid = []
            file.readline()
            for j in range(9):
                lineString = file.readline().strip()
                currentGrid.append([int(num) for num in lineString])
            grids.append(currentGrid)

    return grids

def createSmallerSquares():
    smallerSquares = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            index = (i // 3) + (j // 3) * 3
            smallerSquares[index].append((i, j))

    return smallerSquares

def getSquareElements(r, c):
    global smallerSquares
    for square in smallerSquares:
        if (r, c) in square:
            return square

def getgroupsForCell(rowNumber, colNumber):
    coordsToBeIteratedOver = getSquareElements(rowNumber, colNumber) + [(rowNumber, c) for c in range(9)] + [(r, colNumber) for r in range(9)]
    return coordsToBeIteratedOver

def backtrack(grid):
    row, col = -1, -1
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                row, col = r, c
                break
        if grid[r][c] == 0: break
    if row == -1: return grid
    groups = getgroupsForCell(row, col)

    surroundingNumbers = set([grid[coord[0]][coord[1]] for coord in groups])
    allowed = list(set(range(1, 10)).difference(surroundingNumbers))
    for num in allowed:
        gridCopy = [r[:] for r in grid]
        gridCopy[row][col] = num
        possibility = backtrack(gridCopy)
        if possibility is not None: return possibility
    return None

allGrids = extractGrids()
smallerSquares = createSmallerSquares()
total = 0
for selectedGrid in allGrids:
    solved = backtrack(selectedGrid)
    digits = "".join([str(el) for el in solved[0][:3]])
    total += int(digits)
print (total)