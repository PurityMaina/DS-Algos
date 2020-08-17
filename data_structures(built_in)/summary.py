# Lists are enclosed in brackets:
l = [1, 2, "a"]
print(l)
# Tuples are enclosed in parenthesis and are faster and consume less memory.
t = (1, 2, "a")
print(t)

# Dictionaries are built with curly brackets:
d = {"a":1, "b":2}
print(d)

# Sets are made using the set() builtin function
s = set([1, 2, 3, 4])
print(s)

# Maps returns a list of the results after applying the given function  to each item of a given iterable
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

