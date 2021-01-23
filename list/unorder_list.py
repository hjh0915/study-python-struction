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
        
class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None 
    
    def add(self, item: Node):
        """
        将每一个元素放在一个节点上。
        将新节点的next引用指向当前列表中的第一个节点
        修改列表的头节点，使其指向新创建的节点
        """
        item.setNext(self.head)
        self.head = item

if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(Node(31))
    mylist.add(Node(77))
    mylist.add(Node(17))
    mylist.add(Node(93))
    mylist.add(Node(26))
    mylist.add(Node(54))
    
    # print(mylist.head.getData())
    node = mylist.head 
    while True:
        print('(', node.getData(), 'next -> %s' % (node.getNext()), ')')

        #判断是否为尾部
        if node.getNext() is None:
            break

        node = node.getNext()