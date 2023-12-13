import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile("day-13")

result = 0
reg = re.compile(r'[#\.]')

blocks = [[]]
index = 0

for line in lines:
    if not line == "\n":
        blocks[index].append(reg.findall(line))
        continue
    blocks.append([])
    index += 1

def validSmudge(p1, p2):
    return sum(c1 != c2 for c1, c2 in zip(p1, p2)) == 1

def checkNextPattern(patterns, index, smudges):
    span = 1

    if index == 0:
        if validSmudge(patterns[index], patterns[index + 1]):
            return [True, smudges + 1]
        if patterns[index] == patterns[index + 1]:
            return [True, smudges]

    if index == len(patterns) - 2:
        if validSmudge(patterns[index], patterns[index + 1]):
            return [True, smudges + 1]
        if patterns[index] == patterns[index + 1]:
            return [True, smudges]

    while True:
        if index - span < 0 or index + 1 + span > len(patterns) - 1:
            return [False, smudges]

        if not patterns[index - span] == patterns[index + 1 + span]:
            if validSmudge(patterns[index - span], patterns[index + 1 + span]) and smudges == 0:
                smudges += 1
            else:
                return [False, smudges]

        if index - span == 0 or index + 1 + span == len(patterns) - 1:
            return [True, smudges]

        span += 1

def checkPatterns(patterns):
    smudges = 0
    for index, pattern in enumerate(patterns):
        if index + 1 >= len(patterns) or (not pattern == patterns[index + 1] and not validSmudge(pattern, patterns[index + 1])):
            continue

        if validSmudge(pattern, patterns[index + 1]) and (not index == 0 and not index == len(patterns) - 2):
            smudges += 1

        valid, counter = checkNextPattern(patterns, index, smudges)

        if valid and counter == 1:
            return index + 1

        smudges = 0

    return -1


for blockIndex, patterns in enumerate(blocks):
    print(f'Block number {blockIndex + 1}')

    for pattern in patterns:
        foundMode = None
        foundIndex = 0

        validIndex = checkPatterns(patterns)
        if not validIndex == -1:
            foundMode = "HORIZONTAL"
            foundIndex = validIndex

        if foundMode == None:
            validIndex = checkPatterns([list(x) for x in zip(*patterns)])
            if not validIndex == -1:
                foundMode = "VERTICAL"
                foundIndex = validIndex

        if foundMode == "HORIZONTAL":
            result += (foundIndex * 100)

        if foundMode == "VERTICAL":
            result += foundIndex

        print("  Found mode", foundMode)
        print("  Found index", foundIndex)

        print("")
        break

print("Result", result)


# Answer: 37864 too low
