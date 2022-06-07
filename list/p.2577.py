a = int(input())
b = int(input())
c = int(input())

result = a * b * c

result = list(str(result))

for i in range(0,10,1):
    print(result.count(str(i)))
