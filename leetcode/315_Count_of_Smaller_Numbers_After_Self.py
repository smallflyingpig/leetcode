"""
You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

"""


class Solution0:
   #Time Limit Exceeded
    def get_insert_loc(self, sorted_num, num):
        if len(sorted_num)<1:
            return 0
        if len(sorted_num)==1:
            if num>sorted_num[0]:
                return 0
            else:
                return 1

        mid = len(sorted_num)//2
        if num>sorted_num[mid]:
            return self.get_insert_loc(sorted_num[:mid], num)
        else:
            return mid+self.get_insert_loc(sorted_num[mid:], num)

    def insertData(self, sorted_nums, num):
        if num>sorted_nums[0]:
            return [num]+sorted_nums, len(sorted_nums)

        insert_pos = self.get_insert_loc(sorted_nums, num)
        return sorted_nums[:insert_pos]+[num]+sorted_nums[insert_pos:], len(sorted_nums)-insert_pos
        
    def countSmaller(self, nums):
        if len(nums) < 1:
            return []
        count = [0]
        sorted_nums = [nums[-1]]
        nums = nums[:-1]
        for num in nums[::-1]:
            sorted_nums, insert_pos = self.insertData(sorted_nums, num)
            count = [insert_pos]+count
        return count

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(nums)
        ans = [None]*n
        tmp = []
        for i in range(n-1, -1, -1):
            t = nums[i]
            pos = bisect.bisect_left(tmp, t)
            ans[i] = pos
            tmp.insert(pos, t)

        return ans

def main():
    input_data = [
        [5,2,6,1]
    ]
    s = Solution()
    for data in input_data:
        print(s.countSmaller(data))



if __name__=="__main__":
    main()