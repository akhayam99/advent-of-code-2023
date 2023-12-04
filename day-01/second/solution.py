import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile


# Strips the newline character
pattern = re.compile(r'\d')
sum = 0
for line in getLinesFromFile("day-01/first"):
    matches = pattern.findall(line)
    sum += int(matches[0] + "" + (matches[0] if len(matches) == 1 else matches[len(matches) - 1]))
    print(sum)
