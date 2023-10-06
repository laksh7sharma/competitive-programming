A = [2]
R = 1000
for i in range(1, R):
    if i % 3 == 2: A.append(int(2 / 3 * (i + 1)))
    else: A.append(1)
N = 100

def f(iterationNumber):
    if iterationNumber == 1:
        return A[N - 1], 1
    num = A[N - iterationNumber]
    n, d = f(iterationNumber - 1)
    return n * num + d, n

numerator, denominator = f(N)

print (sum([int(i) for i in str(numerator)]), numerator, denominator)




