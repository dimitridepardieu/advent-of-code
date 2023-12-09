# ================================ Part Two ===================================
import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

gear_ratios = []

for index, line in enumerate(lines):
    # Store in a list the index of each gear found in the current line
    indexes = [index for index, char in enumerate(line) if re.findall(r'\*', char)]

    # Initialize a list of nested lists
    # to store all the numbers adjacent to each gear of the current line
    gear_numbers = [[] for _ in range(len(indexes))]

    # Get patterns of numbers and also their start and end index
    # then store them if they are adjacent to a gear

    # Current line
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for k, i in enumerate(indexes):
            if i in range(match.start() - 1, match.end() + 1):
                gear_numbers[k].append(int(match.group()))

    # Previous line
    if not index == 0:
        previous_matches = re.finditer(r'\d+', lines[index - 1])
        for match in previous_matches:
            for k, i in enumerate(indexes):
                if i in range(match.start() - 1, match.end() + 1):
                    gear_numbers[k].append(int(match.group()))

    # Next line
    if not index == len(lines) - 1:
        next_matches = re.finditer(r'\d+', lines[index + 1])
        for match in next_matches:
            for k, i in enumerate(indexes):
                if i in range(match.start() - 1, match.end() + 1):
                    gear_numbers[k].append(int(match.group()))

    # Store all gear ratios for the current line
    for gn in gear_numbers:
        if len(gn) == 2:
            gear_ratio = gn[0] * gn[1]
            gear_ratios.append(gear_ratio)

print(sum(gear_ratios))
