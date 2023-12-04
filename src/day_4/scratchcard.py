# ============================== Part One =================================
# wn = winning numbers
# mn = my numbers
# mwn = my winning numbers

with open('input.txt', 'r') as f:
    lines = f.readlines()

sum = 0

for line in lines:
    # Parse card numbers
    splits = line.split(':')[1].split('|')
    wn = splits[0].split()
    mn = splits[1].split()

    # Count winning numbers found in the current card
    mwn = []
    for i in wn:
        for j in mn:
            if j == i:
                mwn.append(j)

    if mwn:
        p = 2 ** (len(mwn) - 1)
        sum += p

print(sum)
