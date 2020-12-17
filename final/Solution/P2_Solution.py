class DoubleLinkedList:
    """A base class providing a doubly linked list representation."""

#-------------------------- nested _Node class --------------------------
# nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next' # streamline memory

        def __init__(self, element, prev, next): # initialize node's fields
            self._element = element # user's element
            self._prev = prev # previous node reference
            self._next = next # next node reference

#-------------------------- list constructor --------------------------

    def __init__(self):
        """Create an empty list."""
        self._head = self._Node(None, None, None)
        self._tail = self._Node(None, None, None)
        self._head._next = self._tail
        self._tail._prev = self._head
        self._size = 0 # number of elements

#-------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def add_first(self, e):
        """Add an element to the front of list."""
        self._insert_between(e, self._head, self._head._next)
    
    def __str__(self):
        result = ['head <--> ']
        curNode = self._head._next
        while (curNode._next is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)
    
    #Problem2
    def switch_first(self, l2):
        """Switch first node of self, with first node of l2."""
        node1 = self._head._next
        node2 = l2._head._next

        self._head._next = node2
        l2._head._next = node1

        node2._next._prev = node1
        node1._next._prev = node2

        node1._next, node2._next = node2._next, node1._next
        node1._prev, node2._prev = node2._prev, node1._prev


#test case
def main():
    import random
    test_list = DoubleLinkedList()
    for i in range(8):
        test_list.add_first(random.randint(0, 20))
    print(test_list) #head <--> 9 <--> 7 <--> 5 <--> 10 <--> 4 <--> 18 <--> 1 <--> 11 <--> tail
    l2 = DoubleLinkedList() 
    for i in range(8):
        l2.add_first(random.randint(0, 20))
    print(l2) #head <--> 14 <--> 3 <--> 10 <--> 2 <--> 9 <--> 7 <--> 16 <--> 12 <--> tail
    test_list.switch_first(l2)
    print(test_list) #head <--> 14 <--> 7 <--> 5 <--> 10 <--> 4 <--> 18 <--> 1 <--> 11 <--> tail
    print(l2) #head <--> 9 <--> 3 <--> 10 <--> 2 <--> 9 <--> 7 <--> 16 <--> 12 <--> tail

if __name__ == '__main__':
    main()

