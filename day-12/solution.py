import sys, re
sys.path.append('/Users/aminkhayam/GIT/private/advent-of-code-2023/utils')

from utils import getLinesFromFile
from functools import cache

@cache
def count_occurrences(item, *regex_list, match_count = 0, index = 0):
    if not regex_list:
        return 1 - ("#" in item)

    while (match := regex_list[0].search(item[index:])) and "#" not in item[:index + match.start()]:
        match_count += count_occurrences(item[index + match.end() - 1:], *regex_list[1:])
        index += match.start() + 1

    return match_count

def main():
    pattern = '[.?][#?]{%s}[.?]'
    lines = [[y.split(',') for y in x.split()] for x in getLinesFromFile("day-12")]

    matches = []
    for item, numbers in lines:
        regex_list = [re.compile(pattern % number) for number in numbers]
        matches.append(count_occurrences(f'.{"?".join(item)}.', *regex_list))

    print(f'---------------- Total matches: {sum(matches)}')

main()

# Answer: 7633
