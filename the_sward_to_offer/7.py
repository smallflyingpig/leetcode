# -*- coding:utf-8 -*-
"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
input1: [1,2,3,4,5,6,7],[3,2,4,1,6,5,7]
output1: {1,2,5,3,4,6,7}


"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def get_mid_list(self):
        out = [self.val]
        if self.left is not None:
            left = self.left.get_list()
            out = left + out
        if self.right is not None:
            right = self.right.get_list()
            out = out + right
        return out

    def get_behind_list(self):
        out = [self.val]
        if self.right is not None:
            right = self.right.get_behind_list()
            out = right + out
        if self.left is not None:
            left = self.left.get_behind_list()
            out = left + out
        
        return out
    
    def __str__(self):
        return str(self.get_behind_list())

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 1:
            return TreeNode(pre[0]) 
        if len(pre) == 0:
            return None
        
        cur_node = pre[0]
        left_len = tin.index(cur_node)
        if left_len == 0:
            left_tree = None
        else:
            tin_left = tin[:left_len]
            pre_left = pre[1:left_len+1]
            left_tree = self.reConstructBinaryTree(pre_left, tin_left)
        if left_len == len(pre)-1:
            right_tree = None
        else:
            pre_right = pre[left_len+1:]
            tin_right = tin[left_len+1:]
            right_tree = self.reConstructBinaryTree(pre_right, tin_right)

        head = TreeNode(cur_node)
        head.left = left_tree
        head.right = right_tree
        return head
        

if __name__=="__main__":
    pre = [1,2,3,4,5,6,7]
    tin = [3,2,4,1,6,5,7]
    s = Solution()
    out = s.reConstructBinaryTree(pre, tin)
    print(out)