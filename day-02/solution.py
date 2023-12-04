import sys
import re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

regGame = re.compile(r'Game \d+')
regReds = re.compile(r'\d+ red')
greensReg = re.compile(r'\d+ green')
bluesReg = re.compile(r'\d+ blue')

value = re.compile(r'\d+')

maxRed = 12
maxGreen = 13
maxBlue = 14

result = 0
for line in getLinesFromFile("day-02"):
    exceeded = False
    for red in regReds.findall(line):
        if(int(value.findall(red)[0]) > maxRed):
            exceeded = True

    for green in greensReg.findall(line):
        if(int(value.findall(green)[0]) > maxGreen):
            exceeded = True

    for blue in bluesReg.findall(line):
        if(int(value.findall(blue)[0]) > maxBlue):
            exceeded = True

    if(exceeded == False):
        result += int(value.findall(regGame.findall(line)[0])[0])

print(result)

# Answer: 2512
