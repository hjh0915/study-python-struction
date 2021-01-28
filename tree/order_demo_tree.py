# 改造数据
def split_num(data):
    """
        在本例中是35<4，因为3<4
        将两位数（或以上）拆分比较，选取多为数的第一个数字
    """

    new_data = []
    for n in data:
        # 以35为例
        if n >= 10:
            f = n / 10                  # 会得到一个小数->3.5
            x = (str(f).split('.'))     # ['3', '5]
            final_num = int(x[0])       # 3
            new_data.append(final_num)
        else:
            new_data.append(n)
    return new_data

class Tree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # 插入数据
    def insert(self, data):
        # 将新值与父节点进行比较
        if self.data:  # 非空
            # 以35为例
            if data >= 10 and self.data < 10:   # 需要满足要比的数字为两位数，并且被比的数字为各位数
                f = data / 10                   # 会得到一个小数->3.5
                x = (str(f).split('.'))         # ['3', '5]
                first_num = int(x[0])           # 3

                if first_num < self.data:      #新值小，放左边，小于等于
                    if self.left is None:       #若空，则插入数值
                        self.left = Tree(data)
                    else:                       #若不空，则递归往下查找
                        self.left.insert(data)
                elif first_num >= self.data:     #新值大，放右边
                    if self.right is None:      #若空，则插入数值
                        self.right = Tree(data)
                    else:                       #若不空，则递归往下查找
                        self.right.insert(data)
            else:
                if data < self.data:            #新值小，放左边
                    if self.left is None:       #若空，则插入数值
                        self.left = Tree(data)
                    else:                       #若不空，则递归往下查找
                        self.left.insert(data)
                elif data > self.data:          #新值大，放右边
                    if self.right is None:      #若空，则插入数值
                        self.right = Tree(data)
                    else:                       #若不空，则递归往下查找
                        self.right.insert(data)
        else:
            self.data = data

    # 打印
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.data),
        if self.right:
            self.right.print_tree()

    # 中序遍历
    # Root -> Left -> Right
    def inorder(self, root):
        res = []
        if root:
            res = res + self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res

if __name__ == '__main__':
    data = [3, 2, 4, 7, 6, 35, 9, 8, 44, 55, 66, 77, 88, 99, 999, 9999]
    root = Tree(3)
    for i in data[1:]:
        root.insert(i)
        root.inorder(root)
    root.print_tree()