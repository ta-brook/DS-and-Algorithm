# create function that reverses a strings:
'''
input: "Hi my name is Book" 
result: "kooB si eman ym ih"
'''

import time


str_input = "Hi my name is Book" 

# TODO my own trial
def reverse_string(input_str):
    '''
    time complexity: O(n)
    space complexity: O(n)
    '''
    reverse_index = 17 
    reversed_str = ''

    for idx in range(len(input_str)): # O(n)
        if idx == 0:
            reversed_str = input_str[reverse_index - idx] # O(n) for time and O(1) for space
        else:
            reversed_str = reversed_str + input_str[reverse_index - idx] # O(n) for both time and space
        # print(reversed_str)

    return reversed_str 



# TODO course solution
def reverse(input_str):
    '''
    time complexity: O(n)
    space complexity: O(n)
    '''
    # check input type
    if type(input_str) != str and len(input_str) < 2:
        return 'hmm this not good'

    backwards = []
    total_items = len(input_str)
    for idx in reversed(range(total_items)): # O(n)
        backwards.append(input_str[idx]) # O(n) for both time and space
    # print(backwards)

    return ''.join(backwards)


if __name__ == '__main__':
    start = time.time()
    print(reverse_string(str_input))
    f1 = time.time()
    print(reverse(str_input))
    f2 = time.time()
    print(f'total time used for first function {f1 - start} and for another one is {f2 - f1}')
