class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node):
        # if self.head:
        #     previous = None
        #     current = self.head
        #     next_node = current.get_next()

        #     while current is not None:
        #         current.set_next(previous)
        #         previous = current
        #         current = next_node
        #         if next_node:
        #             next_node = next_node.get_next()
        #     self.head = previous
        # else:
        #     return [None]

        if node.get_next() == None:
            self.head = node
            return
        
        self.reverse_list(node.get_next())
        next_node = node.get_next()
        next_node.set_next(node)
        node.set_next(None)
