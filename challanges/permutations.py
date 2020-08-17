# produces all permutations (ways to arrange) of a given list of items
#  ________________ Using Itertools   ________________
import itertools

def permutations(n):
    for i in itertools.permutations(n):
        print(i)

n = ['A', 'B', 'C']
permutations(n)
#  ________________ Using Loops   ________________
def permutation(n):
    if len(n) == 0:
        return []
    # one permuatation is possible
    if len(n) == 1:
        return [n]

    temp = []
    for i in range(len(n)):  # Iterate the input
        index = n[i]
        # Generate the remaining list given index
        remaining = n[:i] + n[i+1:]  # stop at current element + start at the next element
        # Generate permutation for remaining elements starting with p
        for p in permutation(remaining):
            temp.append([index] + p)
    return temp


n = ['A', 'B', 'C']
for p in permutation(n):
    print(p)