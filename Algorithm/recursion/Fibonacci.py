''''
Given a number of n return the index value of the Fibonacci sequence, where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
the pattern of the sequence is that each value is the sum of the previous values, that means that for N=5 -> 2+3

'''


def fibonacciIterative(n):
    F = [0, 1]
    for idx in range(n):
        F[0], F[1] = F[1], F[0] + F[1]
    return F[0]


def fibonacciRecursive(n):
    '''
    let's say n = 4
    fibonacciRecursive(fibonacciRecursive(fibonacciRecursive(4)))

    1. n=4 : fibonacciRecursive(fibonacciRecursive(f(3) + f(2))
    2. n=3 : fibonacciRecursive(f(2) + f(1))
    3. n=2 : 1

    '''
    if n <= 2:
        return 1
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


print(fibonacciIterative(8))
print(fibonacciRecursive(8))
