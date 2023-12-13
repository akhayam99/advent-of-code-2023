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

def checkPattern(patterns, index):
    span = 1

    if index == 0 and patterns[index] == patterns[index + 1]:
        return True

    if index == len(patterns) - 2 and patterns[index] == patterns[index + 1]:
        return True

    while True:
        if index - span < 0 or index + 1 + span > len(patterns) - 1:
            return False

        if not patterns[index - span] == patterns[index + 1 + span]:
            return False

        if index - span == 0 or index + 1 + span == len(patterns) - 1:
            return True
        span += 1

for blockIndex, patterns in enumerate(blocks):
    # print(f'Block number {blockIndex + 1}')

    for pattern in patterns:
        foundMode = None
        foundIndex = 0
        for index, pattern in enumerate(patterns):
            if index + 1 >= len(patterns) or not pattern == patterns[index + 1]:
                continue

            if checkPattern(patterns, index):
                foundMode = "HORIZONTAL"
                foundIndex = index + 1
                break

        if foundMode == None:
            for index, pattern in enumerate(verticalPatterns := [list(x) for x in zip(*patterns)]):
                if index + 1 >= len(verticalPatterns) or not pattern == verticalPatterns[index + 1]:
                    continue
                if checkPattern(verticalPatterns, index):
                    foundMode = "VERTICAL"
                    foundIndex = index + 1
                    break

        if foundMode == "HORIZONTAL":
            result += (foundIndex * 100)

        if foundMode == "VERTICAL":
            result += foundIndex

        # print("  Found mode", foundMode)
        # print("  Found index", foundIndex)

        # print("")
        break

print("Result", result)
