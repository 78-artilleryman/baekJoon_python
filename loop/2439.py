x = int(input())

for i in range(0,x,1):
    
    for a in range(1,x-i,1):
        print(' ',end='')
    
    for y in range(0,i+1,1):
        print('*',end='')
    print()