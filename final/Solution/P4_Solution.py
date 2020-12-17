class SimpleTree:
    def __init__(self, element, left=None, right=None, parent=None):
        self._element = element
        self._left = left
        self._right = right
        self._parent = parent

    def __str__(self):
        return str(self._element)


#Problem4
"""Displays a simple tree in preorder. Can’t use recursion."""
def pre_order_print(root):
    stack = [root]
    while len(stack) > 0:
        top = stack.pop()
        print(top._element, end = " ")
        if top._right:
            stack.append(top._right)
        if top._left:
            stack.append(top._left)
            
#test case
tree = SimpleTree("1")
tree._left = SimpleTree("2")
tree._right = SimpleTree("3")
tree._left._left = SimpleTree("4")
tree._left._right = SimpleTree("5")
tree._right._right = SimpleTree("8")
tree._right._right._left = SimpleTree("6")
tree._right._right._right = SimpleTree("7")

pre_order_print(tree) #1 2 4 5 3 8 6 7
