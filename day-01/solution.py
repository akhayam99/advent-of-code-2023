import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile as GL, printResult

printResult(sum([int((el := re.compile(r'\d').findall(l))[0] + "" + el[len(el) - 1]) for l in GL("day-01")]))

# Answer: 55447
