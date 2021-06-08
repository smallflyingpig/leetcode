# -*- coding:utf-8 -*-
"""
利用堆排序找到最小的K个数
"""
class MinHeap(object):
    def __init__(self, size, min_flag=True):
        self.size = size
        if min_flag:
            self.func = lambda x,y:x<y 
        else:
            self.func = lambda x,y:x>y 
        self.data = []
    def push(self, d):
        self.data.append(d)
        self.update()
        if len(self.data)>self.size:
            self.data = self.data[1:]
            if len(self.data)>1:
                self.data = [self.data[0]] + self.data[1:]
                self.update_subtree(0)
            
    def pop(self):
        if len(self.data) < 1:
            return None
        if len(self.data) == 1:
            d, self.data = self.data[0], []
            return d 
        d, self.data = self.data[0], self.data[1:]
        self.data = [self.data[-1]] + self.data[:-1]
        self.update_subtree(0)
        return d 
        
    def update(self):
        idx = len(self.data)-1
        while idx>0:
            par_idx = (idx-1)//2
            if self.func(self.data[par_idx], self.data[idx]):
                break
            else:
                self.data[par_idx], self.data[idx] = self.data[idx], self.data[par_idx]
                self.update_subtree(par_idx)
                idx = par_idx
                continue 
                
    def update_subtree(self, idx):
        left_son_idx = idx*2+1
        right_son_idx = idx*2+2
        if left_son_idx < len(self.data):
            if self.func(self.data[idx], self.data[left_son_idx]):
                pass
            else:
                self.data[idx], self.data[left_son_idx] = self.data[left_son_idx], self.data[idx]
                self.update_subtree(left_son_idx)
        if right_son_idx < len(self.data):
            if self.func(self.data[idx], self.data[right_son_idx]):
                pass
            else:
                self.data[idx], self.data[right_son_idx] = self.data[right_son_idx], self.data[idx]
                self.update_subtree(right_son_idx)
            
        
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k>len(tinput):
            return []
        min_heap = MinHeap(k, min_flag=False)
        for d in tinput:
            min_heap.push(d)
        
        rtn = []
        while True:
            d = min_heap.pop()
            if d is None:
                break
            else:
                rtn.append(d)
        return rtn[::-1]
            