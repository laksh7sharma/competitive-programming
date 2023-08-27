from math import gcd

triples = []
N = 1000
end = 1_500_000
count = 0
lengths = [0 for i in range(end)]
original = set()

for b in range(1, N):
    for a in range(b + 1, N):
        A, B, C = a**2 - b**2, 2 * a * b, a**2 + b ** 2
        L = A + B + C
        if gcd(A, B) == 1:
            if L <= end:
                original.add(L)

for i in range(1, end):
    if i in original:
        for j in range(i, end, i):
            lengths[j] += 1

for i, el in enumerate(lengths):
    if el == 1:
        count += 1

print (count)
