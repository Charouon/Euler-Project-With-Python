# number = int(input('Enter your number: '))

# def all_triangle_numbers(n):
#     for i in range(1, n + 1):
#         triangle = (i ** 2 + i)//2
#         print(triangle)
        
# all_triangle_numbers(number)

import math
 
def divs(x) :
    num=0
    for i in range(1,int(math.sqrt(x))+1) :
        if x%i==0 : num+=2
    if math.sqrt(x)==int(math.sqrt(x)) : num+=1
    return num
 
def solve(x) :
    i=0; tri=0
    while(1) :
        i+=1; tri+=i
        if divs(tri)>x : return tri
 
print(solve(500))

def divisor(n):
    j = 1
    mylist = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            j+=1
            mylist.append(i)
    mylist.append(n)
    print("divisor =", (mylist))


divisor(solve(500))

