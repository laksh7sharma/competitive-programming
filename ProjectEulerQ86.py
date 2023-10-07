from math import sqrt
from functools import partial

def calculateDistance(a, x, y, z):
    return sqrt(y**2 + (a - x)**2) + sqrt(a**2 + z**2)

def order(x, y, z):
    l1 = [(x, y, z), (x, z, y), (y, x, z), (y, z, x), (z, x, y), (z, y, x)]
    s1 = set(l1)
    return list(s1)

def calculateShortestDistance(x, y, z):
    global binaryIterations
    orderings = order(x, y, z)
    allDistances = []
    for sequence in orderings:
        x, y, z = sequence
        currentDimensions = partial(calculateDistance, x=x, y=y, z=z)
        lowerBound = 0
        upperBound = x
        for i in range(binaryIterations):
            middleValue = (lowerBound + upperBound) / 2
            distanceEnd = currentDimensions(upperBound)
            distanceStart = currentDimensions(lowerBound)
            if distanceEnd > distanceStart:
                upperBound = middleValue
            else:
                lowerBound = middleValue
        shortestDistance = currentDimensions(middleValue)
        shortestDistanceRounded = round(shortestDistance, 3)
        allDistances.append(shortestDistanceRounded)
    shortestDistanceRounded = min(allDistances)
    return shortestDistanceRounded

M = 100
binaryIterations = 10
count = 0

print (calculateShortestDistance(3, 5, 6))

for x in range(1, M):
    for y in range(x, M):
        for z in range(y, M):
            shortestDistanceRounded = calculateShortestDistance(x, y, z)
            if shortestDistanceRounded == int(shortestDistanceRounded):
                duplicates = 3 - len({x, y, z})
                if duplicates == 0: factor = 6
                elif duplicates == 1: factor = 3
                else: factor = 1
                count += factor

print(count)
# answer is 1818, execution time is 39s