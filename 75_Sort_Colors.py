"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.


Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


result:

Runtime: 36 ms, faster than 81.37% of Python3 online submissions for Sort Colors.
Memory Usage: 13.1 MB, less than 84.09% of Python3 online submissions for Sort Colors.


"""




class Solution:
    def next_data_idx(self, nums, start_idx, end_idx, step, cond):
        next_idx = end_idx
        for idx, num in enumerate(nums[start_idx:end_idx:step]):
            if cond(num):
                next_idx = idx*step+start_idx
                break
        return next_idx


    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find first not 0
        idx = 0
        prob_idx = 0
        while idx<len(nums):
            prob_0 = self.next_data_idx(nums, prob_idx, len(nums), 1, lambda x: x!=0)
            if prob_0 == len(nums):
                return
            next_0_idx = self.next_data_idx(nums, prob_0+1, len(nums), 1, lambda x:x==0)
            prob_idx = prob_0
            if next_0_idx == len(nums):
                break
            else:
                nums[prob_0], nums[next_0_idx] = nums[next_0_idx], nums[prob_0]
            idx = next_0_idx


        idx = prob_idx
        prob_idx = prob_idx
        while idx<len(nums):
            prob_0 = self.next_data_idx(nums, prob_idx, len(nums), 1, lambda x: x!=1)
            if prob_0 == len(nums):
                return
            next_0_idx = self.next_data_idx(nums, prob_0+1, len(nums), 1, lambda x:x==1)
            prob_idx = prob_0
            if next_0_idx == len(nums):
                break
            else:
                nums[prob_0], nums[next_0_idx] = nums[next_0_idx], nums[prob_0]
                
            idx = next_0_idx

        

            



def main():
    s = Solution()
    input_data = [
        [2,0,2,1,1,0],
        [1,2,0,0],
        [0,1]
    ]

    for data in input_data:
        s.sortColors(data)
        print(data)


if __name__=="__main__":
    main()