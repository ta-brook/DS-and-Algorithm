class myArray:
    def __init__(self):
        self.length = 0
        self.data = {}
    
    def __len__(self):
        return self.length

    def __str__(self) -> str:
        return f'myArray length: {self.length}, \ndata: {self.data}'

    def get(self, index):
        '''
        get the array
        '''
        return self.data[index]
    
    def push(self, item):
        '''
        add new item at the end of array
        item: str
        '''
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        '''
        delete the lastest item
        '''
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        '''
        delete item by index
        index: int
        '''
        item = self.data[index]
        self.shift_items(index)
        return item

    def shift_items(self, index):
        '''
        this function is to replace the deleted index with the next one
        index: int
        '''
        for idx in range(index, self.length  - 1): # look into the array as index (2, 5-1)
            self.data[idx] = self.data[idx + 1] # replace 2 with 3, 3 with 4
        del self.data[self.length - 1] # delete index 4
        self.length -= 1


new_array = myArray()
new_array.push('hi')
new_array.push('you')
new_array.push('!')
# new_array.pop()
new_array.delete(2)
new_array.push('are')
new_array.push('nice')
print(str(new_array))
# print(new_array.data, new_array.length)