lst = [1, -2, -3, -4, 5, 6, -7]

temp = []
for i in range(0, len(lst)):
    if lst[i] < 0 and i < len(lst):
        temp.append(lst[i])
    elif lst[i + 1] < 0 and i + 1 < len(lst):
        temp.append(lst[i + 1])
    elif lst[i + 2] < 0 and i + 2 < len(lst):
        temp.append((lst[i + 2]))

print(temp)
