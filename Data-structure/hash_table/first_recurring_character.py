'''
Google question
which one is got repeated first. if no then return undefined

give an array = [2,5,1,2,3,5,1,2,4]
return 2

given an array = [2,1,1,2,3,5,1,2,4]
return 1

given an array = [2,3,4,5]
return undefined
'''

array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
array2 = [2,1,1,2,3,5,1,2,4]
undefined = [2, 3, 4, 5]

# TODO my own trial


def first_recurring_char(arr):  # O(n^2)
    '''
    my idea is to create a nested loop and loop for each number in array
    '''
    # check data type
    if len(arr) == 0:
        return 'input array is empty'

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]

    return 'undefined'


# TODO class solution
def firstRecurringCharacter2(arr):  # O(n)
    map = {}
    for i in range(len(arr)):
        # print(map)
        if arr[i] in map.keys():
            return arr[i]
        else:
            map[arr[i]] = i

    return 'undefined'


print(first_recurring_char(array2))
print(firstRecurringCharacter2(array2))
