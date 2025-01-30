numbers = [[1,2,-4], [6,-1,3], [-12,7,8], [12, -4, 5]]
res = []


for numbers_list in numbers:
    n = numbers_list
    r = 0
    for number in n:
        if number > 0:
            r = r + number

    print(r)
