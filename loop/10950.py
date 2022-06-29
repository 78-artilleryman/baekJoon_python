x = int(input())
sum1 = []

for i in range(0,x,1):
    y,z = map(int,input().split(' '))
    sum1.append(y+z)

for i in range(0,x,1):
    print(sum1[i])
