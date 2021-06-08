"""
Given a collection of intervals, merge all overlapping intervals.

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


result:

Runtime: 52 ms, faster than 60.02% of Python3 online submissions for Merge Intervals.
Memory Usage: 14.5 MB, less than 68.27% of Python3 online submissions for Merge Intervals.

"""


class Solution:
    def merge_interval(self, interval1, interval2):
        if interval2[0]<=interval1[1]:
            return [[interval1[0], max(interval1[1], interval2[1])]]
        else:
            return [interval1, interval2]

    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x:x[0])
        if len(intervals)<=1:
            return intervals
        out_list = [intervals[0]]
        for interval in intervals:
            out_list = out_list[:-1]+self.merge_interval(out_list[-1], interval)
        return out_list

        



def main():
    s = Solution()
    input_datas = [
        [[1,3],[2,6],[8,10],[15,18]],
        [[1,4],[4,5]]
    ]
    for data in input_datas:
        print(s.merge(data))


if __name__=="__main__":
    main()