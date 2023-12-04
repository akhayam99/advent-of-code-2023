import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNewMaxValue

result = 0

for line in getLinesFromFile("day-02"):
    maxRed, maxGreen, maxBlue = 0, 0, 0

    maxRed = getNewMaxValue(line, re.compile(r'\d+ red'), maxRed)
    maxGreen = getNewMaxValue(line, re.compile(r'\d+ green'), maxGreen)
    maxBlue = getNewMaxValue(line, re.compile(r'\d+ blue'), maxBlue)

    result += (maxRed * maxGreen * maxBlue)

print(result)

# Answer: 67335
