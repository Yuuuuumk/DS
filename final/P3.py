class ArrayQueue():

    DEFAULT_CAPACITY = 10   
    
    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Queue is Empty") 
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is Empty")
        ans = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return ans

    def enqueue(self, e):
        if self._size == len(self._data):
            raise Exception("Queue is Full")
        loc = (self._front + self._size) % len(self._data)
        self._data[loc] = e
        self._size += 1

    def __str__(self):
        return str(self._data)


class SimpleTree:
    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right

    def __str__(self):
        return str(self._element)


#Problem3
"""
:param tree: SimpleTree -- Initial call is the root node.
:return: Int – the maximum tree width
"""
def max_width(tree):
    pass

#test case
tree = SimpleTree("1")
tree._left = SimpleTree("2")
tree._right = SimpleTree("3")
tree._left._left = SimpleTree("4")
tree._left._right = SimpleTree("5")
tree._right._right = SimpleTree("8")
tree._right._right._left = SimpleTree("6")
tree._right._right._right = SimpleTree("7")

print(max_width(tree)) #3