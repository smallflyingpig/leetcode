"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

input1: [[1,2],[3,4]]
output1: [1,2,4,3]
"""
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        H, W = len(matrix), len(matrix[0])
        i,j = 0,0
        rtn = []
        while H>0 and W>0:
            rtn += matrix[i][j:j+W-1]
            j += W-1

            rtn += [matrix[_i][j] for _i in range(i, i+H-1)]
            i += H-1

            if H==1 or W==1:
                rtn.append(matrix[i][j])
                break
            rtn += matrix[i][j:j-(W-1):-1]
            j -= W-1

            rtn += [matrix[_i][j] for _i in range(i,i-(H-1),-1)]
            i -= H-1

            i += 1
            j += 1
            H -= 2
            W -= 2
        return rtn
                