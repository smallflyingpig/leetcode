# -*- coding:utf-8 -*-
"""
给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode:TreeLinkNode):
        # write code here
        # 此节点有右子树
        if pNode.right:
            temp = pNode.right
            while temp:
                result = temp
                temp = temp.left
            return result
        # 此节点没有右子树
        while pNode:
            if pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                pNode = pNode.next
            else:
                return None
            
            