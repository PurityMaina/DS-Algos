# memoization - store value for recent call so future calls do not
fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value =2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    # cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 10001):
    print(n, "-", fibonacci(n))
