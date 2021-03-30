#!/usr/bin/python3

n = 600851475143
p = 2
s = 0

while (p*p <= n):

    if (n % p == 0):
        n //= p
        s+=1
        print ('prime' ,s ,p)
    else:
        p += 2 if p>2 else 1
print ('prime', s+1 ,n ,  "\n so big prime is", n )