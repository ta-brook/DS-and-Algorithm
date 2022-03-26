# What is the Big O of the below function? (Hint, you may want to go line by line)

def fun_challenge(input):
    a  = 10 # O(1)
    a = 50 + 3 # O(1)

    for idx in range(len(input)): # O(n)
        stranger = True # n*O(1)
        a += 1 # n*O(1)

    return a # O(1)

# total O notation is O(1 + 1 + n + n*1 + n*1 +1) = O(3n +3)
# from O(3n +3) can be simplified to O(n)