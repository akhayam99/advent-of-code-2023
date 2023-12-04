import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getLiteralValue


# Strips the newline character
pattern1 = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
pattern2 = re.compile(r'(\d|one(?!ight)|two(?!ne)|three(?!ight)|four|five(?!ight)|six|seven(?!ine)|eight(?!wo)|nine(?!ight))')

result = 0

for line in getLinesFromFile("day-01"):
    first, last = pattern1.findall(line), pattern2.findall(line)
    result += int(getLiteralValue(first[0]) + getLiteralValue(last[len(last) - 1]))

print(result)

# Answer: 54706
