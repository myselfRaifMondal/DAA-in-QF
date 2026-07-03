returns = [2, -1, 4, 1, 3]

maximum = returns[0]

for value in returns:
    if value > maximum:
        maximum = value
print(maximum)