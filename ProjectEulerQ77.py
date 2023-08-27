triples = []
N = 10000
allPrimes = []

# generates all the prime numbers up to N

arr = [1 for i in range(N)]
for i in range(2, N):
    if arr[i]:
        allPrimes.append(i)
        for j in range(2 * i, N, i):
            arr[j] = 0

maxNum = 100
numPrimes = sum(arr[2:maxNum])
allPrimes = allPrimes[:numPrimes]

ways = [[0 for i in range(maxNum)] for j in range(maxNum)]

for prime in allPrimes:
    ways[prime][prime] = 1

for n in range(1, maxNum):
    for i, p in enumerate(allPrimes):
        if i == 0: previousPrime = 0
        else: previousPrime = allPrimes[i - 1]
        if p > n:
            if n != previousPrime:
                ways[n][n] = ways[n][previousPrime]
            break
        ways[n][p] += ways[n][previousPrime] + ways[n - p][p]
    for i in range(1, maxNum):
        if ways[n][i] == 0:
            ways[n][i] = ways[n][i - 1]

for n in range(maxNum):
    if ways[n][-1] > 5000:
        print (n)
        break

# for n in range(maxNum):
#     # number of ways to get to n using prime at most n = all the ways we can get to that number
#     print (ways[n][n], n)