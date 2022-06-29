x = int(input())
sum1 = []
sum2 = []
result = []

for i in range(0,x,1):
    y,z = map(int,input().split(' '))
    sum1.append(y)
    sum2.append(z)
    result.append(y+z)

for i in range(0,x,1):
    print('Case #{}: {} + {} = {}'.format(i+1,sum1[i],sum2[i],result[i]))
   