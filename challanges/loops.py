#nested-for loop

import sys
n = [1,2,3,4,5]

for i in range(len(n)):
    print("First For loop", i, end=' ')
    for j in range(len(n)+1):
        print("Second For loop", j)

#Mathematical Table
for i in range(1,11):
   for j in range(1,11):
      k=i*j
      print (k, end=' ')
   print()