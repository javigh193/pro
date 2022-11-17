values = [10, [50, 60, 70]]
flattened_values = []
for value in values:
    if type(value) is list:
        flattened_values.extend(value)
    else:
        flattened_values.append(value)
print(flattened_values)
