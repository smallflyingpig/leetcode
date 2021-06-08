# -*- coding:utf-8 -*-
"""
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""
import heapq

class MaxHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def __len__(self):
        return len(self.data)
    
class MinHeap:
    def __init__(self):
        self.data = []

    def top(self):
        return self.data[0]

    def push(self, val):
        heapq.heappush(self.data, val)

    def pop(self):
        return heapq.heappop(self.data)
    
    def __len__(self):
        return len(self.data)
    
class Solution:
    def __init__(self):
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()
    def Insert(self, num):
        # write code here
        if len(self.max_heap)==0:
            self.max_heap.push(num)
            return
        elif len(self.min_heap)==0:
            self.min_heap.push(num)
            return
        else:
            pass
        
        top_left = self.max_heap.top()
        top_right = self.min_heap.top()
        if num>top_left:
            self.min_heap.push(num)
        
            if len(self.min_heap)>len(self.max_heap):
                d = self.min_heap.pop()
                self.max_heap.push(d)
        else:
            self.max_heap.push(num)
            
            if len(self.max_heap)>len(self.min_heap)+1:
                d = self.max_heap.pop()
                self.min_heap.push(d)
                
        
    def GetMedian(self):
        # write code here
        if len(self.max_heap)==len(self.min_heap):
            return (self.max_heap.top()+self.min_heap.top())/2
        else:
            return self.max_heap.top()


if __name__=="__main__":
    data = [1,3,8,7,9,2,4,5,6,0,10]
    s = Solution()
    for d in data:
        s.Insert(d)
    print(s.GetMedian())
