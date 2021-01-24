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

    def length(self):
        """
        遍历链表、记录访问过多少个节点
        引用能与None作比较
        """
        current = self.head 
        count = 0
        while current != None:
            count = count + 1 
            current = current.getNext()
        
        return count 

    def search(self, item: Node):
        """
        精进上述的遍历链表的方式
        在遍历过程中已经找到所需的元素，则可不必再继续遍历
        """
        current = self.head 
        found = False 
        while current != None and not found:
            if current.getData() == item.getData():
                found = True 
            else:
                current = current.getNext()
            
        return found 

    def remove(self, item: Node):
        """
        查找并移除元素
        1、previous指向current上一次访问的节点
        2、先将previous移动到current位置，再移动current
        """
        current = self.head 
        previous = None 
        found = False 
        while not found:
            if current.getData() == item.getData():
                found = True 
            else:
                previous = current 
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.add(Node(31))
    mylist.add(Node(77))
    mylist.add(Node(17))
    mylist.add(Node(93))
    mylist.add(Node(26))
    mylist.add(Node(54))
    
    print(mylist.head.getData())
    print(mylist.search(Node(17)))