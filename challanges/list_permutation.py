# Python function to print permutations of a given list

def permutations(elements):
    if len(elements) <= 1:
        return [elements]

    l = [] #initialize empty list to store current permutation
    for i in range(len(elements)):
        m = elements[i]

        # Extract lst[i] or m from the list.  remLst is
        # remaining list
        remLst = elements[:i] + elements[i + 1:]

        # Generating all permutations where m is first
        # element
        for p in permutations(remLst):
            l.append([m] + p)

    return l


# Driver program to test above function
data = list('123')
for p in permutations(data):
    print (p )