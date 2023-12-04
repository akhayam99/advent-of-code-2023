import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getArrayOfNumbers, extractNumbersFromRow

result = 0
lines = getLinesFromFile("day-03")


for i, line in enumerate(lines):
    j = 0
    for match in re.compile(r'\*').findall(line):
        j = line.find(match, j)
        start = j - 1 if j > 0 else 0
        end = j + 2 if j + 2 < len(line) - 1 else len(line) - 1

        tops, bottoms, sides = [], [], []

        if(i > 0):
            tops = getArrayOfNumbers(extractNumbersFromRow(lines, i - 1, start, end))

        if(i < len(lines) - 1):
            bottoms = getArrayOfNumbers(extractNumbersFromRow(lines, i + 1, start, end))

        sides = getArrayOfNumbers(extractNumbersFromRow(lines, i, start, end))
        j += 2

        merged = tops + sides + bottoms

        if(len(merged) == 2):
            result += int(merged[0]) * int(merged[1])

print(result)
