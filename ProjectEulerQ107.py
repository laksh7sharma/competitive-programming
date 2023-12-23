with open('network.txt', 'r') as f:
    lines = f.readlines()
    lines = [line[:-1] for line in lines]
    lines = [line.split(',') for line in lines]
    matrix = []
    initialNumber = 0
    for line in lines:
        arr = []
        for el in line:
            if el == "-":
                arr.append(float("inf"))
            else:
                initialNumber += int(el)
                arr.append(int(el))
        matrix.append(arr)
    initialNumber //= 2

numberNodes = 40
totalCost = 0
nodesList = [0]
connectionsList = [float("inf") for i in range(numberNodes)]
newNode = 0
while len(nodesList) != numberNodes:
    connectionsList[newNode] = float("inf")
    for neighbouringNode, weight in enumerate(matrix[newNode]):
        if neighbouringNode not in nodesList:
            connectionsList[neighbouringNode] = min(connectionsList[neighbouringNode], weight)
    smallestWeight = min(connectionsList)
    newNode = connectionsList.index(smallestWeight)
    totalCost += smallestWeight
    nodesList.append(newNode)

print (initialNumber - totalCost)