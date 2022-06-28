x,y,z = input().split(" ")

x = int(x)
y = int(y)
z = int(z)

if x == y and y== z:
    sum1 = 10000+(x*1000)

elif x == y or y == z or z == x:
    if x == y:
        sum1 = 1000+(x*100)
    elif y == z:
        sum1 = 1000+(y*100)
    else:
        sum1 = 1000+(z*100)
else:
    max1 = max(x,y,z)
    sum1 = max1*100

print(sum1)