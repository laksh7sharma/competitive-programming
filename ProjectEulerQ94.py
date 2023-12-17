from math import gcd, sqrt

N = 10000
aValues = []

for b in range(1, N):
    for a in range(b + 1, N, 2):
        A, B, C = a**2 - b**2, 2 * a * b, a**2 + b ** 2
        if abs(2 * B - C) == 1:
            aValues.append(C)
        elif abs(2 * A - C) == 1:
            aValues.append(C)

print (aValues)

answer = 0

for a in aValues[:-1]:
    A1 = sqrt((3 * a + 1) * (a - 1)) * (a + 1) / 4
    A2 = sqrt((3 * a - 1) * (a + 1)) * (a - 1) / 4
    if A1 == int(A1):
        answer += (3 * a + 1)
    if A2 == int(A2):
        answer += (3 * a - 1)

print (answer)