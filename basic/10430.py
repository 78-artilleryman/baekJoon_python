a,b,c = input().split(' ')

x = int(a)
y = int(b)
z = int(c)

print((x+y)%z)
print(((x%z)+(y%z))%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)