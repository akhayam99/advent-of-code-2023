import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile('day-10')
valid_directions = [
    { 'L': ['d-r', 'l-u'] }, { 'F': ['u-r', 'l-d'] }, { '7': ['u-l', 'r-d'] },
    { 'J': ['d-l', 'r-u'] }, { '|': ['d-d', 'u-u'] }, { '-': ['l-l', 'r-r'] }
]

def updatePath(path, direction):
    match direction:
        case 'u': path[0] -= 1
        case 'r': path[1] += 1
        case 'd': path[0] += 1
        case 'l': path[1] -= 1
    return path

matrix = [re.compile(r'[\w\W]').findall(line.replace('\n', '')) for line in lines]
initial = [i, matrix[i].index('S')] if (i := next((i for i, line in enumerate(lines) if line.count('S') > 0), None)) != None else None

for sequence in ['u', 'r', 'd', 'l']:
    dist = 1
    path = updatePath([initial[0], initial[1]], sequence)
    item = matrix[path[0]][path[1]]

    while (item := matrix[path[0]][path[1]]) != 'S' and sequence != None:
        if((dirs := next((arr[item] for arr in valid_directions if item in arr), None)) == None):
            break

        for value in dirs:
            v1, v2 = value.split('-')
            path = updatePath(path, sequence := v2) if v1 == sequence else path

        dist += 1

    if item == 'S':
        break

print(dist // 2)

# Answer: 7063
