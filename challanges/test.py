# determine if there's a pair of elements that sums up to k
# output is yes or no

input = [1, 3, 7]
k = 8

#create 2 pairs of the array i.e i and j
#sum up the elements
#compare if the pair summation is equal to k
#return yes or no

def sum_of_pairs(input, k):
    sum_set = set()
    for i in range(0, len(input)):
        temp_array = k - input[i]
        if (temp_array in sum_set):
            print("Yes (" + str(input[i]) + ", " + str(temp_array) + ")")
        else:
            print("No")
        sum_set.add(input[i])

sum_of_pairs(input, k)

#big O notation for k is 0(n)
