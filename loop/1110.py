x = int(input())
y = 0

if x // 10 == 0:
    x = x*10

sum1 = x //10
sum2 = x%10
sum3 = sum1+sum2

while True:
    
    sum2 = sum2 * 10
    sum3 = sum3 % 10
    sum4 = sum2 + sum3
    y = y+1

    if sum4 == x:
        break
    
    sum1 = sum4//10
    sum2 = sum4%10
    sum3 = sum1+sum2
print(y)