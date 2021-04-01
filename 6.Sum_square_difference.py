#!/usr/bin/python3

sum1 = 0
sum2 = 0
for i in range (1 , 101):
    tavan = i**2
    sum1 +=tavan
    print ('for number',i , '=> ' , sum1 )
print ('\n')
print ('ans1 =',sum1)
for j in range (1 , 101):
    sum2+=j
sum2 = sum2**2
print ('ans2 =',sum2)
ans = sum2-sum1
print ("final ans= ", ans)
