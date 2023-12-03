import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

numbers = []

for index, line in enumerate(lines):
    # List of the index of each symbol found in the line
    indexes = [index for index, char in enumerate(line) if re.findall(r'[^\w.\n]', char)]

    # Isolate patterns of number and their start index
    matches = re.finditer(r'\d+', line)
    for match in matches:
        for i in indexes:
            if i in range(match.start() - 1, match.end() + 1):
                numbers.append(int(match.group()))

    if not index == 0:
        previous_matches = re.finditer(r'\d+', lines[index - 1])
        for match in previous_matches:
            for i in indexes:
                if i in range(match.start() - 1, match.end() + 1):
                    numbers.append(int(match.group()))

    if not index == len(lines) - 1:
        next_matches = re.finditer(r'\d+', lines[index + 1])
        for match in next_matches:
            for i in indexes:
                if i in range(match.start() - 1, match.end() + 1):
                    numbers.append(int(match.group()))

print(sum(numbers))
