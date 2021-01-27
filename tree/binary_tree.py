class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None 

    def insertLeft(self, newNode):
        """插入左子节点"""

        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t 

    def insertRight(self, newNode):
        """插入右子节点"""

        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t 

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key 

    # def preorder(self):
    #     """前序遍历"""

    #     print(self.key)
    #     if self.leftChild:
    #         self.left.preorder()
    #     if self.rightChild:
    #         self.right.preorder()

if __name__ == '__main__':
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())

    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())

    r.insertRight('c')
    r.getRightChild().setRootVal(eval('3'))
    print(r.getRightChild().getRootVal())