# -*- coding:utf-8 -*-
"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
input0: {8,8,#,9,#,2,#,5},{8,9,#,2}
output0: true

input1: {8,#,8,#,9,#,2,#,5},{8,#,9,3,2}
output1: false
"""
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None or pRoot1 is None:
            return False
        return self.IsSubTree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        

    def IsSubTree(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if not (pRoot1.val == pRoot2.val):
            return False
        return self.IsSubTree(pRoot1.left, pRoot2.left) and self.IsSubTree(pRoot1.right, pRoot2.right)

    @staticmethod
    def printTree(root: TreeNode) -> List[List[str]]:
        # 求最大深度
        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            return 1 + max(left, right)

        depth = maxDepth(root)
        # 二维矩阵宽度
        wid = 2**depth - 1
        res = [[''] * wid for _ in range(depth)]

        # DFS
        def dfs(root, depth, start, end):
            # 当前根节点放在(start+end)/2这个中间位置
            res[depth - 1][(start + end) // 2] = str(root.val)
            if root.left:
                dfs(root.left, depth + 1, start, (start + end) // 2)
            if root.right:
                dfs(root.right, depth + 1, (start + end) // 2, end)

        dfs(root, 1, 0, wid)
        return res


def construct_binary_tree(tree_str):
    tree_list = tree_str[1:-1].split(',')
    head = TreeNode(float(tree_list[0]))
    cur = head
    pre_layer_nodes = [head]
    cur_layer_nodes = []
    tree_list.pop(0)
    while len(tree_list)>0:
        # print(tree_list)
        if len(pre_layer_nodes)>0:
            cur = pre_layer_nodes.pop()
            val = tree_list.pop(0)
            if val != '#':
                cur.left = TreeNode(float(val))
                cur_layer_nodes.append(cur.left)
            if len(tree_list)>0:
                val = tree_list.pop(0)
                if val != '#':
                    cur.right = TreeNode(float(val))
                    cur_layer_nodes.append(cur.right)
        else:
            pre_layer_nodes = cur_layer_nodes
            cur_layer_nodes = []
    return head



if __name__ == "__main__":
    tree1 = "{8,8,#,9,#,2,#,5}"
    tree2 = "{8,9,#,2}"
    tree1, tree2 = construct_binary_tree(tree1), construct_binary_tree(tree2)
    s = Solution()
    for l in s.printTree(tree1):
        print(l)
    for l in s.printTree(tree2):
        print(l)
    print(s.HasSubtree(tree1, tree2))
            



