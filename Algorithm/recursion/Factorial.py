'''
Write two function that find any factorial.


'''


def find_factorial_recursive(number):
    '''
    O(n)
    '''
    if number == 2:
        return 2
    return number * find_factorial_recursive(number-1)


def find_factorial_iterative(number):
    '''
    O(n)
    '''
    # result = 1
    # while number > 0:
    #     result = result * number
    #     number -= 1

    result = 1
    for idx, num in enumerate(list(range(number))[::-1]):
        result = (num+1) * result

    return result


print(find_factorial_iterative(8))
print(find_factorial_recursive(8))
