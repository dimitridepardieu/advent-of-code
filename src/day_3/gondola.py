# ================================ Part One ===================================
import re

with open('example.txt', 'r') as f:
    lines = f.readlines()

numbers = []

for index, line in enumerate(lines):
    # Store in a list the index of each gear found in the current line
    indexes = [index for index, char in enumerate(line) if re.findall(r'[^\w.\n]', char)]

    # Get patterns of numbers and also their start and end index
    # then store them if they are adjacent to a gear

    # Current line
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for i in indexes:
            if i in range(match.start() - 1, match.end() + 1):
                numbers.append(int(match.group()))

    # Previous line
    if not index == 0:
        previous_matches = re.finditer(r'\d+', lines[index - 1])
        for match in previous_matches:
            for i in indexes:
                if i in range(match.start() - 1, match.end() + 1):
                    numbers.append(int(match.group()))

    # Next line
    if not index == len(lines) - 1:
        next_matches = re.finditer(r'\d+', lines[index + 1])
        for match in next_matches:
            for i in indexes:
                if i in range(match.start() - 1, match.end() + 1):
                    numbers.append(int(match.group()))

print(sum(numbers))
