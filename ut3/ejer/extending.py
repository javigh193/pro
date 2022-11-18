# values = [10, [50, 60, 70]]
# flattened_values = []
# for value in values:
#     if type(value) is list:
#         flattened_values.extend(value)
#     else:
#         flattened_values.append(value)
# print(flattened_values)

values = [10, [50, [49, 67], 70]]
flattened_values = []
# supongo que es flat hasta que se demuestre lo contrario
flat = True
for value in values:
    if type(value) is list:
        flat = False
while not flat:
    for value in values:
        if type(value) is list:
            flattened_values.extend(value)
        else:
            flattened_values.append(value)
    # supongo que es flat hasta que se demuestre lo contrario
    flat = True
    for value in flattened_values:
        if type(value) is list:
            flat = False
print(flattened_values)
