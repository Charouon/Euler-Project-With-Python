#!/usr/bin/python3


sum = 0
j = 0
sum2=0
def is_prime(n):
    avval = True
    for i in range(2, n):
        if n % i == 0:
            avval = False
            break
    return avval



for i in range (2 , 1_000_000):
    if is_prime(i):
        sum +=1
        sum2 = sum2+ i
        print ('number', sum , '=',  i ,   )
        j+=1
        if sum == 6:
            print ('\n sum =', sum2)
            break

