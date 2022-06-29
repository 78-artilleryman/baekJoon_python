sum1 = []

while True:
    x,y = map(int,input().split(' '))
    sum1.append(x+y)

    if x == 0 and y == 0:
        break

sum1.pop()
for i in range(0,len(sum1),1):
    print(sum1[i])

