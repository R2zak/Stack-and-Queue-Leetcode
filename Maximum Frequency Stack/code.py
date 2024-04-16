from collections import deque
from collections import defaultdict 
class FreqStack:
    def __init__(self):
        self.d=defaultdict(list)
        self.elements=dict()
        self.mx=0
    def push(self, val: int) -> None:
        if val not in self.elements:
            self.elements[val]=1
        else:
            self.elements[val]+=1
        self.d[self.elements[val]].append(val)
        if self.elements[val]>self.mx:
            self.mx=self.elements[val]
    def pop(self) -> int:
        end=self.d[self.mx].pop()
        self.elements[end]-=1
        if not self.d[self.mx]:
            self.mx -= 1
        return end
