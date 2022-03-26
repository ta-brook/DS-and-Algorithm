# given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
'''
for example:
    array_1 = ['a', 'b', 'c', 'x']
    array_2 = ['z', 'y', 'i']
should return False
--------------
    array_1 = ['a', 'b', 'c', 'x']
    array_2 = ['z', 'y', 'x']
should return True
'''

# 2 parameters
# return true or false

array_1 = ['a', 'b', 'c', 'x']
array_2 = ['z', 'y', 'i']
array_3 = ['z', 'y', 'x']


# nested loop
def duplicate_items(arr1, arr2):  # O(a*b)
    for idx in range(len(arr1)): # O(n)
        for jdx in range(len(arr2)): # O(n)
            if arr1[idx] == arr2[jdx]:
                return True
    return False


# TODO the course ideas
# hash table
'''
array_1 ==> dict {
    a: True,
    b: True,
    c: True,
    x: True
}
array_2[index] == array_1.keys()
'''

def contain_common_item(arr1, arr2):
    '''
    loop through first array and create object properties (AKA dict) == items in the array
    then, loop through second array and check if item in second array exists on created object.
    the result should be O(a+b)
    '''
    map = {}
    for idx in range(len(arr1)): # O(n)
        if arr1[idx] not in map.keys():
            item = arr1[idx]
            map[item] = True

    for jdx in range(len(arr2)): # O(n)
        if arr2[jdx] in map.keys():
            return True
    return False


print(duplicate_items(array_1, array_2)) # O(a*b) time | O(1) space
print(contain_common_item(array_1, array_2)) # O(a+b) time | O(n) space

