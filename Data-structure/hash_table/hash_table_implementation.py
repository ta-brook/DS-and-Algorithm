class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash = 0
        for idx in range(len(key)):
            hash = (hash + ord(key[idx]) * idx) % len(self.data)
        return hash

    '''
    create function get & set
        set is to create a new data in hash
        get is to get the specific data from hash
    '''

    def set(self, key, value):  # O(1)
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

        return self.data

    def get(self, key):  # O(n)
        address = self._hash(key)
        current_bucket = self.data[address]
        if current_bucket:
            for idx in range(len(current_bucket)):
                if current_bucket[idx][0] == key:
                    return current_bucket[idx][1]
        return None

    def keys(self): # O(n)
        keys_array = []
        for idx in range(len(self.data)):
            if self.data[idx]:
                keys_array.append(self.data[idx][0][0])
        return keys_array

    def values(self): # O(n)
        value_array = []
        for idx in range(len(self.data)):
            if self.data[idx]:
                value_array.append(self.data[idx][0][1])
        return value_array


my_hash_table = HashTable(38)
print(my_hash_table._hash('mango'))
my_hash_table.set('mango', 10000)
my_hash_table.set('apple', 54)
my_hash_table.set('orange', 2)
print(my_hash_table.keys())
print(my_hash_table.values())
