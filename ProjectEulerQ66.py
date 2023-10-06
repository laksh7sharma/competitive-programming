from math import sqrt
import time

def f(n, numSquares):
    squares = list(i ** 2 for i in range(2, numSquares))
    squareSet = set(squares)
    maximumX = - float("inf")
    correspondingD = 0
    maxSquare = numSquares
    for d in range(2, n + 1):
        if d not in squareSet:
            print (d, flush = True)
            element = 0
            for z in squareSet:
                if z % d == 1 and (z - 1) // d:
                    element = z
            while element == 0:
                maxSquare = maxSquare + 1
                if (maxSquare ** 2) % d == 1:
                    if d == 109:
                        print (((maxSquare ** 2) - 1) / d)
                        print ("progress")
                    if sqrt((maxSquare ** 2 - 1) / d).is_integer():
                        element = maxSquare ** 2
                        maxSquare = numSquares
                        break

            ySquared = (element - 1) // d
            x = sqrt(element)

            if not x ** 2 - d * ySquared == 1:
                print(x, ySquared)
                print ("alert")
            if x > maximumX:
                maximumX = x
                correspondingD = d

    print (maximumX, correspondingD)
    return correspondingD

n, numSquares = 1000, 100
start = time.time()
print (f(n, numSquares))
end = time.time()
print (end - start)