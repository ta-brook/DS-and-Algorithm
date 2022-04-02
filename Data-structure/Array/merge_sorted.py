mergeSortedArray = [[0, 3, 4, 31], [4, 6, 30]]
# result: [0,3,4,4,6,30,31]


# TODO my own trial
def mergeSortedArrays_own_trial(arr1, arr2):  # O(n^2)
    '''
    this is my own trial
    Just used a simple sorted (bubble sort) and it works fine
    '''
    result = []
    result.extend(arr1)
    # print(result)
    result.extend(arr2)
    # print(result)

    for i in range(len(result)):  # O(n)
        for j in range(0, len(result) - i - 1):  # O(n * n)
            # bubble sorted
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    return result

# TODO course solution


def mergeSortedArrays(arr1, arr2):
    '''
    trying to transform code from javacscript ti python
    but we'll face list index out of range instead of undefined
    so, the solution here is to catch an error and replace it with append (because the error will only happend on the last item on arrays)
    BUT if this code shouldn't work with every arrays.
    '''
    merged_array = []
    array_1_item = arr1[0]
    array_2_item = arr2[0]
    i = 1
    j = 1

    # check item
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    while array_1_item or array_2_item: # O(n)

        # print(array_1_item, array_2_item)

        if array_1_item < array_2_item or None:
            merged_array.append(array_1_item)
            try:
                array_1_item = arr1[i]
            except IndexError:
                merged_array.append(array_2_item)
                break
            i += 1
        else:
            merged_array.append(array_2_item)
            try:
                array_2_item = arr2[j]
            except IndexError:
                merged_array.append(array_1_item)
                break
            j += 1

    return merged_array


print(mergeSortedArrays_own_trial(mergeSortedArray[0], mergeSortedArray[1]))
print(mergeSortedArrays(mergeSortedArray[0], mergeSortedArray[1]))
