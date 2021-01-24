class Node:
    def __init__(self, initdata):
        self.data = initdata 
        self.next = None 

    def __str__(self):
        return 'node data: %s' % (self.data)

    def getData(self):
        return self.data 

    def getNext(self):
        return self.next 

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext