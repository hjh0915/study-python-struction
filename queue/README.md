队列
====
有序集合，添加操作在“尾部”，移除操作在“头部”。先进先出

1.创建一个空队列
--------------
Queue()

2.在队列的尾部添加一个元素
----------------------
enqueue(item)

3.从队列的头部移除一个元素
----------------------
dequeue()

实例传土豆淘汰出局的游戏（hot_potato.py）
====================================
此游戏需要理解的一个点是：何为队列（列表）的头部？
我们所理解的是队列（列表）的第一个为头部，但是在此处则为队列（列表）的最后一个为头部，队列（列表）的第一个为尾部。所以，需要对队列（列表）首先进行“倒序”处理

``` py
for name in namelist:
    simqueue.enqueue(name)
```
>>> ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
['Brad', 'Kent', 'Jane', 'Susan', 'David', 'Bill']

双端队列（deque）
==============
与队列类似的有序集合，在哪一端添加和移除没有任何限制。某种意义上，双端队列是栈和队列的结合

1.创建一个空的双端队列
-------------------
Deque()

2.将一个元素添加到双端队列的前端
---------------------------
addFront(item)

3.将一个元素添加到双端队列的后端
---------------------------
addRear(item)

4.从双端队列的前端移除一个元素
--------------------------
removeFront()

5.从双端队列的后端移除一个元素
--------------------------
removeRear()

*回文实例*