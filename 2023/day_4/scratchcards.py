# ============================== Part Two =================================
# wn = winning numbers
# mn = my numbers
# mwn = my winning numbers

with open('input.txt', 'r') as f:
    lines = f.readlines()

# Store number of copies for each card
n = [1 for _ in range(len(lines))]

for index, line in enumerate(lines):
    # Parse card numbers
    splits = line.split(':')[1].split('|')
    wn = splits[0].split()
    mn = splits[1].split()

    # Count winning numbers found in the current card
    count = 0
    for i in wn:
        for j in mn:
            if j == i:
                count += 1

    # Update number of copies for each following card
    if count > 0:
        for i in range(count):
            n[index + i + 1] += 1 * (n[index])

print(sum(n))
