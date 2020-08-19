# A string is said to be palindrome if the reverse of the string is the same as string. ed DAD

# Option 1 -- return reverse of a string
def check_palindrome(s):
    return s == s[::-1]


# Option 2 -- Iterative Method
def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)): # for i in 0 to midpoint
        if str[i] != str[len(str) - 1 - i]: #if item to the left is not equal to the last item after the current
            return False
    return True

def isPalindrome(word):
  midPoint = len(word)//2
  print("****************Midpoint is ***********************", midPoint)
  palindrome = True
  for i in range(0,midPoint):
    print("****************Midpoint is ***********************", midPoint)

    left = word[i]
    print("****************Left is ***********************", left)

    right = word[len(word)-i-1] #takw the length of word then put the index all the way to the end (check the last item after the current)
    print("****************Right is ***********************", right)
    if left!=right:
      palindrome=False
      break
  return palindrome


# Option 3 -- Built in  Method
def is_palindrome(s):
    # copy all elements of s in temp
    r = ''.join(reversed(s))
    if r == s: #check if same with s ir temp == s
        return True

    return False


s = "DAAD"
if check_palindrome(s):
    print("True")
else:
    print("False")
# Option 2
if isPalindrome(s):
    print("True")
else:
    print("False")
# Option 3

if is_palindrome(s):
    print("True")
else:
    print("False")
