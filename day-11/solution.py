import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile("day-11")
pattern = re.compile(r'\W')

galaxies, duplicated_x, duplicated_y = [], [], []

for i, line in enumerate(lines):
    if all(char == '.' for char in pattern.findall(line.replace('\n', ''))):
        duplicated_x.append(i)
    else:
        for y, char in enumerate(line):
            if char == '#':
                galaxies.append((i, y))

for index in range(len(lines)):
    if all(x == '.' for x in pattern.findall(''.join([line[index] for line in lines]))):
        duplicated_y.append(index)

couple_of_galaxies = []

for i1, main in enumerate(galaxies):
    for i2, other in enumerate(galaxies):
        if i1 != i2:
            couple_of_galaxies.append((main, other))


distance = 0
for [galaxy1, galaxy2] in couple_of_galaxies:
    distance_x = abs(galaxy1[0] - galaxy2[0])
    distance_y = abs(galaxy1[1] - galaxy2[1])

    for x in duplicated_x:
        if galaxy1[0] < x < galaxy2[0] or galaxy2[0] < x < galaxy1[0]:
            distance_x += 1

    for y in duplicated_y:
        if galaxy1[1] < y < galaxy2[1] or galaxy2[1] < y < galaxy1[1]:
            distance_y += 1

    distance += distance_x + distance_y

print(distance // 2)

# Answer 9545480
