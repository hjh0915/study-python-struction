树
===
节点与引用
---------
创建一个实例binary_tree.py中的BinaryTree类，其中包含插入左子节点和插入右子节点操作

二叉树
=====
*二叉树的所有子树也都是二叉树*

构建解析树
---------
1、引入栈。为了追踪当前节点及其父节点，在遍历树时用栈记录父节点   
2、先将当前节点压入栈中，当要返回到当前节点的父节点时，就将此父节点从栈中弹出   

二叉树使用实例——(3+(4*5))
-----------------------
1、创建一个空树   
2、读入'('。为根节点添加一个左子节点   
3、读入'3'。将当前节点值设为3，并回到父节点   
4、读入'+'。将当前节点值设为+，并添加一个右子节点，此时新节点为当前节点   
5、读入'('。为当前节点添加一个左子节点，并将其作为当前节点   
6、读入'4'。将当前节点设为4，并回到父节点   
7、读入'*'。与第4步相同   
8、读入'5'。将当前节点设为5，并回到父节点   
9、读入')'。将*的父节点作为当前节点   
10、读入')'。将+的父节点作为当前节点，但是+没有父节点，所以完成。

若是两位数字的实例——(13+(40*5))
============================
1、对于split()内置函数，是针对中间带有空格的字符串（即应该写成"( 13 + ( 40 * 5 ) )"），依据空格来切片   
2、若是没有空格的话，那么在执行到eval(i)时，就会把结果计算出来，所以eval()函数有计算的功能   
3、若是在1和3中间有空格的话，那么会报错（IndexError: ppop from empty list）