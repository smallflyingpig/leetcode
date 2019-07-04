"""
164. Maximum Gap

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.

Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.


result:

Runtime: 48 ms, faster than 58.68% of Python3 online submissions for Maximum Gap.
Memory Usage: 14.6 MB, less than 16.43% of Python3 online submissions for Maximum Gap.

"""

class Solution:
    def maximumGap(self, nums: list) -> int:
        if len(nums)<2:
            return 0
        if len(nums) == 2:
            return abs(nums[0]-nums[1])
        buckets_num = len(nums)
        num_min = min(nums)
        num_range = max(nums)-num_min
        if num_range<2:
            return num_range
        buckets = [[] for _ in range(buckets_num)]
        for num in nums:
            bucket = buckets[((num-num_min)*(buckets_num-1)//num_range)]
            if len(bucket)<1:
                bucket += [num, num]
            else:
                bucket[0], bucket[1] = min(bucket[0], num), max(bucket[1], num)
                
        max_cap = 0
        pre_max = buckets[0][1]
        for bucket in buckets[1:]:
            if len(bucket)<1:
                continue
            max_cap = max(max_cap, bucket[0]-pre_max)
            pre_max = bucket[1]
        return max_cap

def main():
    s = Solution()
    input_data = [
        [3,6,9,1],
        [10]
    ]
    for data in input_data:
        print(s.maximumGap(data))

if __name__ == "__main__":
    main()