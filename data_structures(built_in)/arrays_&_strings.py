# ------------------- Arrays ------------------------ #
# Mutable and behave similarly to lists—except they are “typed arrays” constrained to a single data type.
# Square brackets can be used to access elements of the string.
import array

arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])

# Arrays have a nice repr:
print(" ************** Arrays ****************** ")
print(arr)

# Arrays are mutable:
arr[1] = 23.0
print(arr)

#delete elements in array

del arr[1]
print(arr)

# add elements to array
arr.append(42.0)
print(arr)

# Arrays are "typed":
#arr[1] = "hello"
print(arr)#TypeError: must be real number, not str


# ------------------- Strings ------------------------ #
#  literals in python are surrounded by either single quotation marks, or double quotation marks.
print(" ************** Strings  ****************** ")
# Slicing -  return a range of characters by  start index and the end index, separated by a colon.
b = "Hello, World!"

print(" --- Slicing ---")
#a[start:stop]  # items start through stop-1
#a[start:]      # items start through the rest of the array
#a[:stop]       # items from the beginning through stop-1
#a[:]           # a copy of the whole array
print(b[:])  # all items in the array
print(b[0:5])  # all items in the array
print(b[0:5:1])  # all items in the array
print(b[::])  # all items in the array


print(b[-1])  # last item in the array
print(b[-2:])  # last two items in the array
print(b[:-2])  # everything except the last two items
print(b[::-1])     # all items in the array, reversed
print(b[1::-1])    # the first two items, reversed
print(b[:-3:-1])   # the last two items, reversed
print(b[-3::-1])   # everything except the last two items, reversed
print(b[2:5]) # Negative Indexing - Use negative indexes to start the slice from the end of the string


print(" --- Length ---")

# String Length - To get the length of a string, use the len() function.
a = "Eng.Purity, Maina"
print(len(a))

print(" --- Strip ---")
#strip() - removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) #returns "Hello, World!"

print(" --- Lower ---")
# lower() - returns the string in lower case:
print(a.lower())

print(" --- Upper ---")
# upper() - returns the string in upper case:
print(a.upper())

print(" --- Replace ---")
#replace() - replaces a string with another string:
print(a.replace("H", "J"))

print(" --- Split ---")
# split() - splits the string into substrings if it finds instances of the separator:
print(a.split(","))# returns ['Hello', ' World!']

print(" --- Checks ---")
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

print(" --- Concatenation ---")
#Concatenation - Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

print(" --- Formatting ---")
# Formatting - we cannot combine strings and numbers
# format() method to insert numbers into strings:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print(" --- Escape ---")
# escape character is a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "Hello\nWorld!"
print(txt)
