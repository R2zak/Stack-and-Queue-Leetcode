class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head is None
    def push(self, item):
        self.head = Node(item, self.head)
    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item
    @property
    def peek(self):
        return self.head.item
    def reverse(self):
        new=None
        link=None
        while self.head!=None:
            new=Node(self.head.item,link)
            link=new
            self.head=self.head.next
        self.head=new
class MyQueue(object):
    def __init__(self):
        self.head=Stack()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.head:
            self.head.push(x)
        else:
            self.head.reverse()
            self.head.push(x)
            self.head.reverse()
    def pop(self):
        """
        :rtype: int
        """
        return self.head.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.head.peek

    def empty(self):
        """
        :rtype: bool
        """
        return self.head.is_empty()
