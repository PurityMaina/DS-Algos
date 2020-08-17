# ------------------- Arrays ------------------------ #
#   mutable and behave similarly to lists—except they are “typed arrays” constrained to a single data type.
# Square brackets can be used to access elements of the string.
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])

# Arrays have a nice repr:
arr
array('f', [1.0, 1.5, 2.0, 2.5])

# Arrays are mutable:
>>> arr[1] = 23.0
>>> arr
array('f', [1.0, 23.0, 2.0, 2.5])

>>> del arr[1]
>>> arr
array('f', [1.0, 2.0, 2.5])

>>> arr.append(42.0)
>>> arr
array('f', [1.0, 2.0, 2.5, 42.0])

# Arrays are "typed":
>>> arr[1] = 'hello'
TypeError: "must be real number, not str"





# ------------------- Strings ------------------------ #
#  literals in python are surrounded by either single quotation marks, or double quotation marks.

# Slicing -  return a range of characters by  start index and the end index, separated by a colon.