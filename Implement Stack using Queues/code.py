class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Queue:
    def __init__(self):
        self.head=None
    def push(self,val):
        self.head=Node(val,self.head)
    def pop(self):
        pp=self.head
        if pp:
            if pp.next:
                while pp.next.next!=None:
                    pp=pp.next
                num=pp.next.item
                pp.next=None
                return num
            else:
                num=self.head.item
                self.head=None
                return num
    def reverse(self):
        new=None
        link=None
        while self.head!=None:
            new=Node(self.head.item,link)
            link=new
            self.head=self.head.next
        self.head=new
    def empty(self):
        if self.head==None:
            return True
        return False
class MyStack:
    def __init__(self):
        self.head=Queue()
    def push(self, x: int) -> None:
        self.head.push(x)
    def pop(self) -> int:
        if self.head.head:
            self.head.reverse()
            op=self.head.pop()
            self.head.reverse()
        return op
    def top(self) -> int:
        return self.head.head.item if self.head.head else None
    def empty(self) -> bool:
        return self.head.empty()
