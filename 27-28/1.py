
s = 0
with open('numbers.txt') as f:
    lines = f.readlines()
    print(lines)
    for line in lines:
        print(line)
        s += int(line)
print(s)