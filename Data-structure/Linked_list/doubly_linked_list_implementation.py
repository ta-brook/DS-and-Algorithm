class Node():
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Node Object: {self.__class__.__name__}"


class doubly_linked_lists():
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def __len__(self):
        return self.length

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        return f"{self.__class__.__name__} \nitems: {nodes} \nhead: {self.head.value} \ntail: {self.tail.value} \nlength: {repr(self.length)}"

    def append(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value, self.head)
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self

    def traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node.next
            counter += 1
        return current_node

    def insert(self, index, value):
        if index >= self.length:
            self.append(value)
        elif index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            leader = self.traverse_to_index(index-1)
            new_node.next = leader.next
            leader.prev = leader
            leader.next = new_node
            leader.next.prev = new_node
            self.length += 1
            return self

    # def remove(self, index):
    #     leader = self.traverse_to_index(index-1)
    #     unwanted_node = leader.next
    #     leader.next = unwanted_node.next
    #     self.length -= 1
    #     return self


myLinkedList = doubly_linked_lists(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2, 99)
# myLinkedList.remove(2)
print(myLinkedList)
