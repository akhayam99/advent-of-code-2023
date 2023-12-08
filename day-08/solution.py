import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile

lines = getLinesFromFile("day-08")

myMap = []
paths = [char for char in lines[0].replace('\n', '')]

pattern = re.compile(r'\w{3}')
for line in lines:
    if ' = ' not in line:
        continue
    values = pattern.findall(line)
    myMap.append({values[0]: values[1:len(values)]})


match, counter, index = "AAA", 0, 0
while match != "ZZZ":
    index = 0 if index >= len(paths) else index
    combination = next((dizionario[match] for dizionario in myMap if match in dizionario), None)
    match = combination[1] if paths[index] == "R" else combination[0]
    index += 1; counter += 1

print(counter)

# Answer: 19667
