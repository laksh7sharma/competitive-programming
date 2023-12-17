from collections import defaultdict

def f(n):
    if n in sumFactors:
        del sumFactors[n]

    for number in reversedSumFactors[n]:
        if number != n:
            f(number)

N = 1_000000
sumFactors = {i : 0 for i in range(1, N)}

for i in range(1, N // 2 + 1):
    num = 2 * i
    while num < N:
        sumFactors[num] += i
        num += i

reversedSumFactors = defaultdict(list)

for key, value in sumFactors.items():
    reversedSumFactors[value].append(key)
chains = []

numbersToBeRemoved = [1] + [key for key, value in sumFactors.items() if value > N] + [key for key in sumFactors.keys() if key == sumFactors[key]]

for number in numbersToBeRemoved:
    f(number)

previous = set()
cycles = []

for start in sumFactors.keys():
    if start in previous: continue
    cur, next = start, sumFactors[start]
    cycle = [cur]
    while next != start:
        cur, next = next, sumFactors[next]
        cycle.append(cur)
        if next in cycle: break

    if next == start:
        cycles.append(cycle)
        previous = previous.union(cycle)

for cycle in cycles:
    print (cycle, len(cycle))

