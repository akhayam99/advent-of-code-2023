import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getLiteralValue


# Strips the newline character
pattern1 = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
pattern2 = re.compile(r'(\d|one(?!ight)|two(?!ne)|three(?!ight)|four|five(?!ight)|six|seven(?!ine)|eight(?!wo)|nine(?!ight))')

sum = 0
current_line = 0
for line in getLinesFromFile("day-01"):
    first = pattern1.findall(line)
    last = pattern2.findall(line)
    current_line += 1
    print(current_line, " --- ", getLiteralValue(first[0]) + "" + getLiteralValue(last[len(last) - 1]), " --- ", line)
    sum += int(getLiteralValue(first[0]) + "" + getLiteralValue(last[len(last) - 1]))

print(sum)
