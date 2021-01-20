class LListUnderflow(ValueError):
    pass

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, data):
        self._head = Node(data, self._head)
    
    def pop(self):
        if self._head is None:
            raise LListUnderflow("in pop")
        e = self._head.data
        self._head = self._head.next
        return e 
    
    def append(self, data):
        if self._head is None:
            self._head = Node(data)
            return 
        p = self._head
        while p.next is not None:
            p = p.next 
        p.next = Node(data)

    def pop_last(self):
        if self._head is None:
            raise LListUnderflow("in pop")
        p = self._head
        if p.next is None:
            e = p.data
            self._head = None
            return e 
        while p.next.next is not None:
            p = p.next 
        e = p.next.data
        p.next = None 
        return e 

    def find(self, pred):
        p = self._head 
        while p is not None:
            if pred(p.data):
                return p.data
            p = p.next 

    def printall(self):
        p = self._head 
        while p is not None:
            print(p.data, end='')
            if p.next is not None:
                print(', ', end='')
            p = p.next 
        print('')

    def elements(self):
        p = self._head 
        while p is not None:
            yield p.data
            p = p.next
    
    def filter(self, pred):
        p = self._head 
        while p is not None:
            if pred(p.data):
                yield p.data 
            p = p.next 

    def length(self):
        i = 0 
        p = self._head 
        while p is not None:
            i += 1 
            p = p.next
        return i 

def div5(n:int):
    if n % 5 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)
    mlist1.printall()

    print(mlist1.find(div5))

    print([i for i in mlist1.elements()])

    x = mlist1.filter(div5)        
    print(x.__next__())
    print(x.__next__())
    print(x.__next__())

    print([i for i in mlist1.filter(div5)])

    print(mlist1.pop())
    mlist1.printall()
    print(mlist1.pop_last())
    mlist1.printall()

    print(mlist1.length())