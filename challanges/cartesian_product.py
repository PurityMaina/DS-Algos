#How to  create data as all possible pairs of containers

#1 : list comprehension
# initialize list and tuple
test_list = [1, 4, 6, 7]
test_tup = (1, 3)

res = [(a, b) for a in test_tup for b in test_list]

print("The Cartesian Product is : " + str(res))

