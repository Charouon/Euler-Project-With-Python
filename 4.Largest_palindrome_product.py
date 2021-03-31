#!/usr/bin/python3

def find ():
  sum = 0
  mylist = []

  for i in range(100, 1000):
    for j in range(100, 1000):
      if (str(i * j) == str(i * j)[ : : -1]):
        sum +=1
        #print(sum , 'find ' ,i ,'*', j , ' = ', str(i * j)  )
        mylist.append(str(i*j))

  mylist = list(map(int, mylist))
  print(max(mylist))

find ()
