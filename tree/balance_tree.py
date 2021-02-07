import copy

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class AVLTree(object):
    def __init__(self):
        self.root = None

    # 左子树的高度
    def left_height(self, node):  # 开始传入根结点，后面传入每个子树的根结点
        if node is None:
            return 0
        return self.tree_height(node.left)

    # 右子树的高度
    def right_height(self, node):  # 开始传入根结点，后面传入每个子树的根结点
        if node is None:
            return 0
        return self.tree_height(node.right)

    # 以该结点为根结点的树的高度
    def tree_height(self, node):
        if node is None:
            return 0
        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1

    # 进行左旋转
    def left_rotate(self, node):
        '''
            创建新的结点，以当前根结点的值,
            把新结点的左子树设为当前结点的左子树,
            把新结点的右子树设为当前结点的右子树的左子树,
            把当前结点的值替换成它的右子结点的值,
            把当前结点的右子树设置成当前结点的右子树的右子树,
            把当前结点的左子结点设置成（指向）新的结点
        '''
        if node is None:
            return

        new_node = copy.deepcopy(node)
        new_node.left = node.left
        new_node.right = node.right.left
        node.val = node.right.val
        node.right = node.right.right
        node.left = new_node


    # 进行右旋转
    def right_rotate(self, node):
        '''
            创建新的结点，以当前根结点的值,
            把新结点的右子树设为当前结点的右子树,
            把新结点的左子树设为当前结点的左子树的右子树,
            把当前结点的值替换成它的左子结点的值,
            把当前结点的左子树设置成当前结点的左子树的左子树,
            把当前结点的右子结点设置成（指向）新的结点
        '''
        if node is None:
            return

        new_node = copy.deepcopy(node)  # 深度复制拷贝
        new_node.right = node.right
        new_node.left = node.left.right
        node.val = node.left.val
        node.left = node.left.left
        node.right = new_node

    # 添加结点
    def add(self, val):
        node = TreeNode(val)
        if self.root is None:
            self.root = node
            return
        s = [self.root]
        while s:
            temp_node = s.pop(0)
            # 判断传入结点的值和当前子树结点的值关系
            if node.val < temp_node.val:
                if temp_node.left is None:
                    temp_node.left = node
                    return
                else:
                    s.append(temp_node.left)
            if node.val >= temp_node.val:
                if temp_node.right is None:
                    temp_node.right = node
                    return
                else:
                    s.append(temp_node.right)

    def jude_node(self, node): 
        '''判断二叉排序树是否需要调整（是否达到平衡）'''

        if self.right_height(node) - self.left_height(node) > 1:  # 右子树高于左子树
            # 如果它的右子树的左子树的高度数 大于 它的右子树的右子树高度数
            if node.right and self.left_height(node.right) > self.right_height(node.right):
                # 先对当前结点的右子结点（右子树）进行-> 右旋转
                self.right_rotate(node.right)
                # 再对当前结点进行左旋转
                self.left_rotate(self.root)
            else:
                # 直接进行左旋转
                self.left_rotate(self.root)

            # 注意这个return 因为判断为一种情况，就要总结判断
            return 

        if self.left_height(node) - self.right_height(node) > 1:  # 左子树高于右子树
            # 如果它的左子树的右子树的高度数 大于 它的左子树的左子树的高度数
            if node.left and self.right_height(node.left) > self.left_height(node.left):
                # 先对当前结点的左子结点（左子树）进行-> 左旋转
                self.left_rotate(node.left)
                # 再对当前结点进行右旋转
                self.right_rotate(self.root)
            else:
                # 直接进行右旋转
                self.right_rotate(self.root)

    # 中序遍历
    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.val, end=" ")
        self.inorder(node.right)


    # 前序遍历（主要看根结点的变化）
    def preorder(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)


if __name__ == '__main__':
    t = AVLTree()
    data = [3, 2, 4, 7, 6, 35, 9, 8, 44, 55, 66, 77, 88, 99, 999, 9999]
    for i in data:
        t.add(i)
        t.jude_node(t.root)
    print("中序遍历结果为：")
    t.inorder(t.root)
    print('\n')
    print("旋转后，前序遍历结果为：")
    t.preorder(t.root)
    print('\n')
    print("树的高度为:", t.tree_height(t.root))
    print("左子树高度为：", t.left_height(t.root))
    print("右子树高度为：", t.right_height(t.root))