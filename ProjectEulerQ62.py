from collections import defaultdict, Counter

cubes = [str(i**3) for i in range(1, 10000)]
cubesByFrequencies = defaultdict(list)

for cube in cubes:
    cubesByFrequencies[tuple(sorted(list(int(char) for char in cube)))].append(cube)

def f(n):
    possible = []
    selected = {k : v for k, v in cubesByFrequencies.items() if len(v) >= n}
    for v in selected.values():
        arr = [len(el) for el in v]
        counter = Counter(arr)
        mostCommonLength, mostCommonFrequency = counter.most_common(1)[0]
        if mostCommonFrequency == n:
            selectedCubes = [int(el) for el in v if len(el) == mostCommonLength]
            possible.append(selectedCubes)
    possible.sort(key = lambda x : min(x))
    return min(possible[0])

print (f(5))