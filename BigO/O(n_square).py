# O(n^2) - Quadratic Time

boxes = [idx for idx in range(1,6)]
boxes_str = ['a', 'b', 'c', 'd', 'e']

def log_all_pars_of_array(array):
    '''
    Quadratic time - O(n^2)
    '''
    for idx in range(len(array)): # O(n)
        for jdx in range(len(array)): # O(n)
            print(array[idx], array[jdx]) # O(n*n)

log_all_pars_of_array(boxes_str)

# O(n*n) = O(n^2)