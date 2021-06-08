"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.


Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

intervals = [[1,5]], newInterval=[2,7]
output: [[1,7]]


result:

Runtime: 44 ms, faster than 89.84% of Python3 online submissions for Insert Interval.
Memory Usage: 14.9 MB, less than 83.47% of Python3 online submissions for Insert Interval.


"""

class Solution:
    def insert(self, intervals, newInterval):
        if len(intervals)<1:
            return [newInterval]
        if intervals[0][0]>newInterval[1]:
            return [newInterval]+intervals
        if intervals[-1][1]<newInterval[0]:
            return intervals+[newInterval]

        start_idx = len(intervals)
        for idx, interval in enumerate(intervals):
            if interval[1]>=newInterval[0]:
                start_idx = idx
                break
        # print(start_idx)
        start = min(intervals[start_idx][0], newInterval[0])

        end_idx = len(intervals)
        for idx, interval in enumerate(intervals[start_idx:]):
            if interval[0]>newInterval[1]:
                end_idx = idx+start_idx
                break
        # sprint(end_idx)
        end = max(intervals[end_idx-1][1], newInterval[1])
        
        out_list = intervals[:start_idx]+[[start, end]]+intervals[end_idx:len(intervals)]
        return out_list

def main():
    s = Solution()
    intervals = [
        [[1,3],[6,9]],
        [[1,2],[3,5],[6,7],[8,10],[12,16]],
        [[1,5]],
        [[1,5]]
    ]
    new_intervals = [
        [2,5],
        [4,8],
        [2,7],
        [6,8]
    ]
    for interval, new_interval in zip(intervals, new_intervals):
        print(s.insert(interval, new_interval))


if __name__=="__main__":
    main()