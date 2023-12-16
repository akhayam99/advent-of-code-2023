import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

result = 0
colors = [['red', 12], ['green', 13], ['blue', 14]]

def isExceeded(line, max, reg):
    for item in reg.findall(line):
        if(int(getNumbers(item)[0]) > max):
            return True
    return False

for l in getLinesFromFile("day-02"):
    if not [True for c in colors if isExceeded(l, c[1], re.compile(r'\d+ %s' % c[0]))]:
        result += int(getNumbers(re.compile(r'Game \d+').findall(l)[0])[0])

print(result)

# Answer: 2512
