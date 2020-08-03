# determine if there's a pair of elements that sums up to k
# output is yes or no

input = [1, 3, 7]
k = 8

#create 2 pairs of the array i.e i and j
#sum up the elements
#compare if the pair summation is equal to k
#return yes or no

def sum_of_pairs(input, k):
    n = len(input)
    for i in range(0, n): #pair 1
        for j in range(i + 1, n): #pair 2
            if (input[i] + input[j] == k): #check the sum of pairs
                print("Yes", sep="")
            else:
                print("No", sep="")

sum_of_pairs(input, k)

#big O notation for k is 0(n^2)