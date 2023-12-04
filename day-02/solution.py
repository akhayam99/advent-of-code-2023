import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile, getNumbers

maxRed = 12
maxGreen = 13
maxBlue = 14

result = 0



for line in getLinesFromFile("day-02"):
    exceeded = False

    for red in re.compile(r'\d+ red').findall(line):
        if(int(getNumbers(red)[0]) > maxRed):
            exceeded = True
            break

    if (exceeded == False):
        for green in re.compile(r'\d+ green').findall(line):
            if(int(getNumbers(green)[0]) > maxGreen):
                exceeded = True
                break

    if (exceeded == False):
        for blue in re.compile(r'\d+ blue').findall(line):
            if(int(getNumbers(blue)[0]) > maxBlue):
                exceeded = True
                break

    if(exceeded == False):
        result += int(getNumbers(re.compile(r'Game \d+').findall(line)[0])[0])

print(result)

# Answer: 2512
