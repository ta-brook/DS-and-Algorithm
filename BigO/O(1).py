# O(1) - Constant time
# Doesn't matter how many item in array have we only take the exact index that we need
# O(1) = 1

boxes = [idx for idx in range(6)]

def log_first_two_boxes(boxes):
    print(boxes[0]) # O(1)
    print(boxes[1]) # O(1)

log_first_two_boxes(boxes) # O(1) + O(1) = O(2)