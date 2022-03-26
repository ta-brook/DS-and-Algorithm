# O(n) linear time
# O(n) is refer to the incresing of number of input affect number of operation as well (linear).
# O(n) = n

import time

nemo = ['nemo'] 
large = ['nemo' for idx in range(100)] 
massive = ['nemo' for idx in range(10000)] 

def find_nemo(array):
    '''
    Linear time - O(n)
    '''
    t0 = time.time()
    for idx in range(len(array)):
        if array[idx] == 'nemo':
            print('Found nemo')
    t1 = time.time()
    print(f'Call to find Nemo took {t1-t0} ms')

find_nemo(nemo) # O(1)
find_nemo(large) # O(100)
find_nemo(massive) # O(10000)