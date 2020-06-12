from linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if storage is less than capacity
        # then add new item to tail
        # make last item the current
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        if self.storage.length == self.capacity:
            self.current.value = item
            if self.current is self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def __len__(self):
        return self.storage.length

    def get(self):
        list_buffer_contents = []
        node = self.storage.head
        while node is not None:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents
