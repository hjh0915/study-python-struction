import sys 
sys.path.append("..") 
from basic.stack import Stack

import binary_tree 
import operator

def buildParseTree(fpexp):
    """解析树构造器"""

    fplist = fpexp.split()
    pStack = Stack()
    eTree = binary_tree.BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent 
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError("不知名的构造器：" + i)
    
    return eTree

def preorder(tree):
    """前序遍历"""

    if tree:
        print(tree.getRootVal())

        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    """中序遍历"""

    if tree != None:
        inorder(tree.getLeftChild())

        print(tree.getRootVal())
        inorder(tree.getRightChild())

def postorder(tree):
    """后序遍历"""

    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        
        print(tree.getRootVal())

def postordereval(tree):
    """计算二叉解析树的函数（重写build_tree.py中的evaluate函数）"""

    opers = {
        '+': operator.add, '-': operator.sub, 
        '*': operator.mul, '/': operator.truediv
    }

    res1 = None 
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()

if __name__ == '__main__':
    x = "( 13 + ( 40 * 5 ) )"
    pre_tree = buildParseTree(x)
    print(preorder(pre_tree))

    in_tree = buildParseTree(x)
    print(inorder(in_tree))

    post_tree = buildParseTree(x)
    print(postorder(post_tree))

    print(postordereval(pre_tree))
    print(postordereval(in_tree))
    print(postordereval(post_tree))