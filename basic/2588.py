x = int(input())
y = int(input())

a = (y//100)*x
b = y%100
c = b%10
b = b//10

b = b*x
c = c*x
print(c)
print(b)
print(a)

print(c+b*10+a*100)