# -*- coding:utf-8 -*-
"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
窗口大于数组长度的时候，返回空

input1:
[2,3,4,2,6,2,5,1],3
output1: 
[4,4,6,6,6,5]

url: https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking&from=cyc_github

"""
import heapq

class MaxHeap:
    def __init__(self):
        self.data = []
        
    def remove(self, val):
        data_new = []
        find_flag = False
        for idx in range(len(self.data)):
            if not find_flag and -self.data[idx] == val:
                find_flag = True
                continue
            else:
                heapq.heappush(data_new, self.data[idx])
        self.data = data_new

    def top(self):
        return -self.data[0]

    def push(self, val):
        heapq.heappush(self.data, -val)

    def pop(self):
        return -heapq.heappop(self.data)
    
    def __len__(self):
        return len(self.data)
    
class Solution1: # max heap
    def __init__(self):
        self.max_heap = MaxHeap()
        self.win_buf = []
    def maxInWindows(self, num, size):
        # write code here
        rtn = []
        if size==0 or size>len(num):
            return rtn
        for d in num:
            if size>len(self.max_heap)+1:
                self.max_heap.push(d)
                self.win_buf.append(d)
            else:
                self.max_heap.push(d)
                self.win_buf.append(d)
                rtn.append(self.max_heap.top())
                self.max_heap.remove(self.win_buf[0])
                self.win_buf = self.win_buf[1:]
        return rtn


class Solution2: # three pointer
    def maxInWindows(self, num, size):
        # write code here
        if size==0 or size>len(num):
            return []
        rtn = []
        max_idx = 0
        for idx in range(size):
            if num[idx]>num[max_idx]:
                max_idx=idx
        rtn.append(num[max_idx])
        idx = size
        cur_idx = idx
        while idx<len(num):
            if idx-max_idx>=size:
                max_idx += 1
                idx = max_idx 
            else:
                if num[idx]>num[max_idx]:
                    max_idx = idx
                if idx==cur_idx:
                    rtn.append(num[max_idx])
                    cur_idx += 1
                idx += 1
            
        return rtn 


if __name__=="__main__":
    num, size = [2,3,4,2,6,2,5,1],3
    s = Solution1()
    print(s.maxInWindows(num, size))