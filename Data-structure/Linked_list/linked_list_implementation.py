# 1 --> 10 --> 99 --> 5 --> 16

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value


class linked_list():
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
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    def prepend(self, value):
        new_node = Node(value, self.head)
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
            leader.next = new_node
            self.length += 1
            return self

    def remove(self, index):
        leader = self.traverse_to_index(index-1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1
        return self

    def reverse(self):
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self


myLinkedList = linked_list(10)
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.prepend(1)
myLinkedList.insert(2, 99)
myLinkedList.remove(2)
myLinkedList.reverse()
print(myLinkedList)
