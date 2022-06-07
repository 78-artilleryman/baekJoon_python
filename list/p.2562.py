y=[]

for i in range(0,9,1):
    y.append(int(input()))

print(max(y))
print(y.index(max(y))+1)
