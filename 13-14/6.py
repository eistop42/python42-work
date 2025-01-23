text = "В1центре1Галактики1находится1сверхмассивная1чёрная1дыра"

t = text.split('1')

s = " ".join(t)
print(s)
print(text.replace('1', ' '))

