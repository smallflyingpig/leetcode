# -*- coding:utf-8 -*-
"""
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

input0: {5,4,#,3,#,2,#,1}
output0: [5,4,3,2,1]

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if root is None:
            return []
        print_node_list = []
        cur_layer_nodes = [root]
        while len(cur_layer_nodes)>0:
            n = cur_layer_nodes.pop(0)
            print_node_list.append(n.val)
            if n.left is not None:
                cur_layer_nodes.append(n.left)
            if n.right is not None:
                cur_layer_nodes.append(n.right)
        return print_node_list