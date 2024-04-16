from collections import deque
from collections import defaultdict 
class FreqStack:
    def __init__(self):
        self.elements=defaultdict(list)
        self.head=deque()
        self.mx=0
    def push(self, val: int) -> None:
        self.head.appendleft(val)
        count=self.head.count(val)
        self.elements[count].append(val)
        if count>self.mx:
            self.mx=count
    def pop(self) -> int:
        end=self.elements[self.mx].pop()
        self.head.remove(end)
        if not self.elements[self.mx]:
            self.mx -= 1
        return end
