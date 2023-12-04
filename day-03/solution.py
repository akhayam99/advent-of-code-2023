import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, hasSymbolsAround


result = 0
lines = getLinesFromFile("day-03")

for i, line in enumerate(lines):
    j = 0
    for match in re.compile(r'\d+').findall(line):
        j = line.find(match, j)
        start = j - 1 if j > 0 else 0
        end = j + len(match) + 1 if j + len(match) + 1 < len(line) - 1 else len(line) - 1

        if(hasSymbolsAround(lines, i, start, end)):
            result += int(match)

        j += len(match) + 1

print(result)

# Answer: 540025
