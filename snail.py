initial = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = []

while initial:
    new_list.append(initial[0])
    initial.pop(0)
    if initial:
        for row in initial:
            if row:
                new_list.append(row[-1])
                row.pop(-1)
    if initial:
        initial[1].reverse()
        new_list.extend(initial[1])
        initial.pop(-1)
        if initial:
            for row in initial[::-1]:
                if row:
                    new_list.append(row[0])
                    row.pop(0)
print(new_list)
print(initial)
"""print(initial[1])
initial.pop(1)
print('NL contains', new_list)
print('original matrix', initial)"""
