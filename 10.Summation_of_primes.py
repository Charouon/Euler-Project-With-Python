def is_prime(x):
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(round(x**0.5))+1,2):
        if x%i==0:
            return False
    else:
        return True

my_input = int(input("Find sum of prime : "))
sum=0
mylist = []

for i in range(2,my_input):
    if is_prime(i)==True:
        sum+=i
        mylist.append(i)
print (mylist)
print ('find' , len(mylist) , 'numbers prime')
print ('sum =' , sum)