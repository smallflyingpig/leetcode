"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
[
  [1,2,8,9],
  [2,4,9,12],
  [4,7,10,13],
  [6,8,11,15]
]
给定 target = 7，返回 true。

给定 target = 3，返回 false。

input1: 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
output1: True

input2: 3,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
output2: false
""" 
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        N = len(array)
        M = len(array[0])
        row = N-1
        col = 0
        while col<M and row>=0:
            cur = array[row][col]
            if cur == target:
                return True
            elif cur < target:
                col += 1
                continue 
            elif cur > target:
                row -= 1
            else:
                pass
        return False
                