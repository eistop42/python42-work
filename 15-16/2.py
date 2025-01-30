numbers = [[1,2,-4], [6,-1,3], [-12,7,8], [12, -4, 5]]
res = []


for i in range(len(numbers)):
    n = numbers[i]

    r = 0
    for k in range(len(n)):
        if n[k] > 0:
            r = r + n[k]

    res.append(r)
print(res)