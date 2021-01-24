链表
====
无序列表

节点类（Node）
------------
```py 
class Node:
    def __init__(self, initdata):
        self.data = initdata 
        self.next = None 
```
一个节点包括两个方面的内容：数据和指向（自我理解为箭头）

``` py
def __str__(self):
    return 'node data: %s' % (self.data)
```
通过__str__函数方法，将指向性的数据展示出来


链表类（UnorderedList）
---------------------
1、初始化一个头节点，并且此头节点为空（self.head = None）   
2、通过添加头节点来添加新的节点   
3、可以增加length()、search(item: Node)、remove(item: Node)进行查询有多少个节点、查找所需元素、移除指定元素的操作   


遍历构建的链表
============
```py
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
```
1、此处的遍历需要使用while而不能使用for   
2、通过打印出node.getData()和node.getNext()更加深刻表示出节点的含义   
3、若判断节点的指向为空则已到尾部，需要通过break将尾部节点也打印出来