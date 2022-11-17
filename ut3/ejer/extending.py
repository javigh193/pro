values = [10, [50, 60, 70]]
plane_values = []
for value in values:
    if type(value) is list:
        plane_values.extend(value)
    else:
        plane_values.append(value)
print(plane_values)
