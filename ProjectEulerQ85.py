def f(height, width):
    total = 0
    for w in range(1, width + 1):
        for h in range(1, height + 1):
            total += (width - w + 1) * (height - h + 1)
    return total

currentClosest = [0, 100000]
N = 100

for w in range(1, N):
    for h in range(1, N):
        diff = abs(f(h, w) - 2 * 10 ** 6)
        if diff < currentClosest[1]:
            currentClosest = [w * h, diff]

print (currentClosest)