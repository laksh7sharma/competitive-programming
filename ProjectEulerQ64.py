from math import floor, sqrt

count = 0
squares = [i ** 2 for i in range(1, 100)]
for k in range(2, 10000):
    if k in squares: continue
    n = floor(sqrt(k))
    arr = [[n, n, 1]]
    repeat = False
    while not repeat:
        a, b, c = arr[-1]
        A = round((floor(c / (sqrt(k) - b))), 1)
        C = round(((k - b**2) / c), 1)
        B = round((C * (A - (b * c) / (k - b ** 2))), 1)
        repeat = [A, B, C] in arr
        arr.append([A, B, C])

    period = len(arr) - 2
    print (k, period)
    if period % 2 == 1:
        # print (k)
        count += 1

print (count)
