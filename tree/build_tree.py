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
            print(i)

            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            print(i)

            currentTree.setRootVal(eval(i))
            print(eval(i)) # 会进行计算，若传入的是没有空格的字符串

            parent = pStack.pop()
            currentTree = parent 
        elif i in '+-*/':
            print(i)

            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            print(i)

            currentTree = pStack.pop()
        else:
            raise ValueError("不知名的构造器：" + i)
    
    return eTree

def evaluate(parseTree):
    """计算二叉解析树的递归函数"""

    opers = {
        '+': operator.add, '-': operator.sub, 
        '*': operator.mul, '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()

if __name__ == '__main__':
    x = "( 13 + ( 40 * 5 ) )"
    t = buildParseTree(x)
    print(evaluate(t))