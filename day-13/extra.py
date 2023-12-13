import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

def isSmudge(p1, p2):
    return sum(c1 != c2 for c1, c2 in zip(p1, p2)) == 1

def process(l, i, s):
    if i == 0 or i == len(l) - 2:
        return [True, s + 1] if isSmudge(l[i], l[i + 1]) else [False, s]

    for j in range(1, 999999):
        if i - j < 0 or i + 1 + j > len(l) - 1:
            return [False, s]

        if not l[i - j] == l[i + 1 + j]:
            if not isSmudge(l[i - j], l[i + 1 + j]) and s == 0:
                return [False, s]
            s += 1

        if i - j == 0 or i + 1 + j == len(l) - 1:
            return [True, s]

def isValid(l):
    for i, el in enumerate(l):
        s = 0
        if i + 1 >= len(l) or (not el == l[i + 1] and not isSmudge(el, l[i + 1])):
            continue

        s += 1 if isSmudge(el, l[i + 1]) and (not i == 0 and not i == len(l) - 2) else 0
        if (fnR := process(l, i, s)) and fnR[1] == 1:
            return i + 1

    return -1

def summarize(l):
    return i * 100 if not (i := isValid(l)) == -1 else isValid([list(x) for x in zip(*l)])

list, result = [], 0
for line in getLinesFromFile("day-13"):
    if not line == "\n":
        list.append(re.compile(r'[#\.]').findall(line)); continue
    result, list = result + summarize(list), []

print(f'\n---------------- Result: {result + summarize(list)} ----------------\n')

# Answer: 44615
