def generateArr():
    allNumb = [[] for i in range(6)]
    allNumbDict = []

    for i in range(6):
        number = 1
        n = 1
        while number < 10**4:
            if i == 0:
                number = n*(n + 1) / 2
            elif i == 1:
                number = n**2
            elif i == 2:
                number = n*(3*n - 1) / 2
            elif i == 3:
                number = n*(2*n - 1)
            elif i == 4:
                number = n*(5*n - 3) / 2
            elif i == 5:
                number = n*(3*n - 2)
            n += 1
            if number >= 10 ** 3:
                allNumb[i].append(str(number))

    for arr in allNumb:
        result = {}
        for el in arr:
            result.setdefault(el[:2], []).append(el[2:4])
        allNumbDict.append(result)

    return allNumbDict

numbers = generateArr()

def generateCyclic(prev, limit, start, used):

    if used + 1 == (1 << limit):
        if prev == start:
            return ""
        else:
            return "-1"
    elif used == 0:
        for j in range(6):
            for key in numbers[0]:
                for val in numbers[0][key]:
                    result = key + val + "-" + generateCyclic(val, limit, key, used | (1 << j))
                    if result[-2:] != "-1":
                        return result
    else:
        for j in range(6):
            if not ((1 << j) & used):
                if prev in numbers[j]:
                    for val in numbers[j][prev]:
                        if val != prev:
                            result = prev + val + "-" + generateCyclic(val, limit, start, used | (1 << j))
                            if result[-2:] != "-1": return result
        return "-1"

n = 3
ans = generateCyclic(None, n, None, 0)
tot = 0
print (ans)
for i in range(0, len(ans) - 1, 5):
    tot += int(ans[i:i + 4])
print (tot)