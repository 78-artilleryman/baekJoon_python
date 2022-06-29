x, y = map(int,input().split(' '))

z = y
y = y-45

if y < 0:
    y = z + 60
    y = y-45
    x = x-1
    if x < 0:
        x = 23

print(x , y)