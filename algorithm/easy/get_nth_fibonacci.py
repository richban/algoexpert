# Nth Fibonacci
# The Fibonacci sequence is defined as follows: the first number of the sequence is 0, the second number is 1, and the nth number is the sum of the (n - 1)th and (n
# -2)th numbers. Write a function that takes in an integer n and returns the nth Fibonacci number.
# Important note: the Fibonacci sequence is often defined with its first two numbers as FO = 0 and F1 = 1. For the purpose of this question, the first Fibonacci
# F0
# number is FO; therefore, getNth Fib (1) is equal to FO, getNthFib(2) is equal to F1, etc..

# def getNthFib(n):
#     # Write your code here.
#     if n == 2:
#         return 1
#     elif n == 1:
#         return 0
#     else:
#         return getNthFib(n-1) + getNthFib(n-2)

def getNthFib(n, cache = {1: 0, 2: 1}):
    """
        O(n) time
        O(n) space
    """
    if n in cache:
        return cache[n]
    else:
        cache[n] = getNthFib(n-1, cache) + getNthFib(n-2, cache)
        return cache[n]

