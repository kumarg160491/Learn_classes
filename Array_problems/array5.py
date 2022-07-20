
# diff = max(n) - min(n)
#
#
# n.sort()
# sub = n[-1] - n[0]
# print(sub)

def find_min_max(n):
    min = 0
    max = 0

    for i in n:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

def cal_diff(v1, v2):
    if v1 > v2:
        return v1 - v2
    else:
        return v2 - v1
n = [1, 6, 4, 0, 3]
x,y=find_min_max(n)
print(cal_diff(x,y))