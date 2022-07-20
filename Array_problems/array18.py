s = 'helsdkfhsdkjhlo'
s = list(s)
if len(s) % 2 == 0:
    s[(len(s) // 2) - 1] = s[(len(s) // 2)] = '*'
else:
    s[(len(s) // 2)] = '*'

print(s)
