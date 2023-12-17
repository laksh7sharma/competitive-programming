def add(a, b): return a + b
def subtract(a, b): return a - b
def divide(a, b): return a / b
def multiply(a, b): return a * b

allowedOperations = [add, subtract, divide, multiply]

def possible(n, used):
    arr = []
    if len(used) == 4: return n == 0

    for num in allowedNumbers:
        if num not in used:
            for op in allowedOperations:
                invserseNumber = op(n, num)
                arr.append(possible(invserseNumber, used + [num]))

    return True in arr

def p(current, index):
    if len(current) == 4: return [current]
    arr = []
    limit = 6 + len(current)
    for nextIndex in range(index + 1, limit):
        futureWays = p(current + [first10[nextIndex]], nextIndex)
        arr.extend(futureWays)
    return arr

first10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
permutations = p([], -1)
maxLimit = 0
best = []

for allowedNumbers in permutations:
    limit = 1
    notFinished = True
    while notFinished:
        notFinished = possible(limit, [])
        limit += 1
    if limit > maxLimit:
        maxLimit = limit
        best = allowedNumbers

print (maxLimit, best)


