from collections import defaultdict

def g(N):
    with open('words.txt', 'r') as f:
        line = f.readline()
        words = [word[1:-1] for word in line.split(',')]

    anagramWords = defaultdict(list)

    for word in words:
        wordLetters = tuple(sorted([letter for letter in word]))
        anagramWords[wordLetters].append(word)

    anagramWords = {k: v for k, v in anagramWords.items() if len(v) >= 2}

    anagramSquares = defaultdict(list)

    squares = [i ** 2 for i in range(1, N)]

    for number in squares:
        squareDigits = tuple(sorted([int(digit) for digit in str(number)]))
        anagramSquares[squareDigits].append(number)

    anagramSquares = {k: v for k, v in anagramSquares.items() if len(v) >= 2}

    return anagramSquares, anagramWords

def flatten(arr):
    a = []
    for el in arr:
        a.extend(el)
    return a

def group(arr):
    pairs = []
    length = len(arr)
    for i in range(length):
        for j in range(i + 1, length):
            pairs.append((arr[i], arr[j]))
    return pairs

def sortByLength(anagrams):
    pairs = flatten([group(v) for v in anagrams.values()])
    pairsLength = defaultdict(list)
    for pair in pairs:
        length = len(str(pair[0]))
        pairsLength[length].append(pair)
    return pairsLength

def generateMap(word, number):
    map = dict()
    numberList = [int(el) for el in str(number)]
    for index, letter in enumerate(word):
        map[letter] = numberList[index]
    return map

def fun(numberPair, wordPair):
    map0 = generateMap(wordPair[0], numberPair[0])
    map1 = generateMap(wordPair[1], numberPair[1])
    if map0 == map1:
        values0 = [val for val in map0.values()]
        return len(values0) == len(set(values0))
    return False

formats = defaultdict(list)
anagramSquares, anagramWords = g(100_000)

squarePairs = sortByLength(anagramSquares)
wordPairs = sortByLength(anagramWords)

successfulMatches = []

for length, arr in wordPairs.items():
    numberPairsOfSameLength = squarePairs[length]
    for wordPair in arr:
        for numPair in numberPairsOfSameLength:
            if fun(numPair, wordPair):
                successfulMatches.append((numPair, wordPair))

answer = 0
for match in successfulMatches:

    answer = max(answer, match[0][0], match[0][1])

print (answer)