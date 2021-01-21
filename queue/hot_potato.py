from basic.queue import Queue 

def hotPotato(namelist, num):
    """传土豆模拟"""

    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            print(simqueue.items)
            simqueue.enqueue(simqueue.dequeue())
    
        simqueue.dequeue()
    return simqueue.dequeue()

if __name__ == '__main__':
    x = ['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad']
    print(hotPotato(x, 7))