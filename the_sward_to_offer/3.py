# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任一一个重复的数字。 例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是2或者3。存在不合法的输入的话输出-1
# input: [2,3,1,0,2,5,3]
# output: 2
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param numbers int整型一维数组 
# @return int整型
#
class Solution:
    def duplicate(self , numbers ):
        # write code here
        num_dict = {}
        for n in numbers:
            if n in num_dict:
                return n 
            else:
                num_dict[n] = n 
        return -1


        