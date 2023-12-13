import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

def validSmudge(p1, p2):
    return sum(c1 != c2 for c1, c2 in zip(p1, p2)) == 1

def processPatterns(patterns, index, smudges):
    if index == 0 or index == len(patterns) - 2:
        return [True, smudges + 1] if validSmudge(patterns[index], patterns[index + 1]) else [False, smudges]

    for j in range(1, 999999):
        if index - j < 0 or index + 1 + j > len(patterns) - 1:
            return [False, smudges]

        if not patterns[index - j] == patterns[index + 1 + j]:
            if not validSmudge(patterns[index - j], patterns[index + 1 + j]) and smudges == 0:
                return [False, smudges]
            smudges += 1

        if index - j == 0 or index + 1 + j == len(patterns) - 1:
            return [True, smudges]

def checkBlock(list):
    for i, el in enumerate(list):
        smudges = 0
        if i + 1 >= len(list) or (not el == list[i + 1] and not validSmudge(el, list[i + 1])):
            continue

        smudges += 1 if validSmudge(el, list[i + 1]) and (not i == 0 and not i == len(list) - 2) else 0
        if (fnResult := processPatterns(list, i, smudges)) and fnResult[1] == 1:
            return i + 1

    return -1

def getResultFromPatterns(patterns):
    if not (position := checkBlock(patterns)) == -1:
        return position * 100
    if not (position := checkBlock([list(x) for x in zip(*patterns)])) == -1:
        return position
    return 0

patterns, result = [], 0
for line in getLinesFromFile("day-13"):
    if not line == "\n":
        patterns.append(re.compile(r'[#\.]').findall(line)); continue
    result, patterns = result + getResultFromPatterns(patterns), []

result += getResultFromPatterns(patterns)

print("Result", result)

# Answer: 44615
