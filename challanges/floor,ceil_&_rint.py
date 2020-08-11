import numpy
input= ['1.1' '2.2' '3.3' '4.4' '5.5']

arr = map(float, input().split())
my_array = numpy.array(arr)

# floor returns the floor of the input element-wise.
print(numpy.floor(my_array))

# ceil returns the ceiling of the input element-wise.
print(numpy.ceil(my_array))

# rint tool rounds to the nearest integer of input element-wise.
print(numpy.rint(my_array))




