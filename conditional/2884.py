x, y = map(int,input().split(' '))
z = int(input())

y = y+z

if y >= 60:
    sum1 = y//60
    sum2 = y%60

    x = x+sum1
    y = sum2

    if x > 23:
        x = x-24
print(x , y)