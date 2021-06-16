# -*- coding:utf-8 -*-
"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

input0: {8,6,10,5,7,9,11}
output0: [[8],[6,10],[5,7,9,11]]

"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        print_list = []
        cur_layer = [pRoot]
        while len(cur_layer)>0:
            cur_out = []
            cur_layer_len = len(cur_layer)
            for _ in range(cur_layer_len):
                n = cur_layer.pop(0)
                cur_out.append(n.val)
                if n.left:
                    cur_layer.append(n.left)
                if n.right:
                    cur_layer.append(n.right)
            print_list.append(cur_out)
        return print_list
        
        