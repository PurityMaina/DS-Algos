#Itertool is a module that provides various functions that work on iterators to produce complex iterators.
import operator
import time
# Defining time

L1 = [1, 2, 3]
L2 = ['a', 'b', 'c']

# Starting time before map function
t1 = time.time()
# Multiplication using maps
a, b, c = map(operator.mul, L1, L2)
# end time after map function
t2 = time.time()
# calculate time taken
print("Result:", a, b, c)
print("Time taken by map function: %.6f"  %(t2 - t1))

# start time
a1 = time.time()
# Multiplication using for loop
for i in range(len(L1)):
    print(L1[i] * L2[i], end = " ")
# end time
a2 = time.time()
# calculate time taken
print("\nTime taken by for loop : %.6f"  %(a2 - a1))






