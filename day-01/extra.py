import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile as GL, getLiteralValue as LV, printResult

p1 = re.compile(r'\d|one|two|three|four|five|six|seven|eight|nine')
p2 = re.compile(r'(\d|one(?!ight)|two(?!ne)|three(?!ight)|four|five(?!ight)|six|seven(?!ine)|eight(?!wo)|nine(?!ight))')

printResult(sum([int(LV(l1 := (p1.findall(r)[0])) + LV((l2 := p2.findall(r))[len(l2) - 1])) for r in GL("day-01")]))

# Answer: 54706
