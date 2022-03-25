# What is the Big O of the below function? (Hint, you may want to go line by line)

def another_fun_challenge(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)
    for idx in range(len(input)): # O(n)
        x = idx + 1 # O(n)
        y = idx + 2 # O(n)
        z = idx + 3 # O(n)

    for jdx in range(len(input)): # O(n)
        p = j * 2 # O(n)
        q = j * 2 # O(n)

    who_am_I = "I don't know" # O(1)

# total O notation is O(1 + 1 + 1 + n + n + n + n + n + n + n + 1) = O(7n +4)
# O(7n +4) can be simplified to O(n)