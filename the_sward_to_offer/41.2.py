# -*- coding:utf-8 -*-
"""
字符流中第一个不重复的字符


请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
后台会用以下方式调用Insert 和 FirstAppearingOnce 函数

string caseout = "";
1.读入测试用例字符串casein
2.如果对应语言有Init()函数的话，执行Init() 函数
3.循环遍历字符串里的每一个字符ch {
Insert(ch);
caseout += FirstAppearingOnce()
}
2. 输出caseout，进行比较。


返回值描述：
如果当前字符流没有存在出现一次的字符，返回#字符。

input1:
google
output1:
ggg#ll

"""
class Solution:
    def __init__(self):
        self.freq = [0 for _ in range(128)]
        self.char_queue = []
        self.first_char = None
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if self.first_char is None:
            return '#'
        else:
            return self.first_char
        
    def Insert(self, char):
        # write code here
        char_int = ord(char)
        if self.freq[char_int] == 0:
            self.freq[char_int] = 1
            self.char_queue.append(char)
            if self.first_char is None:
                self.first_char = char
        else:
            self.freq[char_int] += 1
            if char == self.first_char:
                # update queue
                while len(self.char_queue)>0 and self.freq[ord(self.char_queue[0])]>1:
                    self.char_queue = self.char_queue[1:]
                if len(self.char_queue)>0:
                    self.first_char = self.char_queue[0]
                else:
                    self.first_char = None
            

if __name__=="__main__":
    string = 'google'
    rtn = ''
    solution = Solution()
    for c in string:
        solution.Insert(c)
        rtn += solution.FirstAppearingOnce()
    print(rtn)