class LCList:
    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None
    
    def prepend(self, elem):
        self.p = LNode(elem, self.p)
        if self._rear is None:
            p.next = prepend
            self._rear = p 
        else:
            p.next = self._rear.next  
            self._rear.next = p  

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next 

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None 
        else:
            self._rear.next = p.next 
        return p.elem 

    def printall(self):
        if self.is_empty():
            return 
        p = self._rear.next 
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next 

if __name__ == '__main__':
    mlist1 = LCList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()