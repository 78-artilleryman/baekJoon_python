y =[]

for i in range(0,10,1):
    x = int(input())
    result = x % 42
    y.append(result)

y = set(y)
print(len(y))
