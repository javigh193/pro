dominion = [5, 6, 7, 2, 1, 9, 4, 3]
maxim = dominion[0]
for value in dominion:
    if value > maxim:
        maxim = value
print(maxim)
