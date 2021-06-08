class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1

        best_len = 1 # start, len
        cur_start = 0
        cur_len = 1
        for c in s[1:]:
            try:
                c_idx = s[cur_start:cur_start+cur_len].index(c)
            except ValueError:
                c_idx = -1

            if c_idx<0:
                cur_len += 1
            else:
                if cur_len>best_len:
                    best_len = cur_len
                cur_start = cur_start+c_idx+1
                cur_len = cur_len - c_idx
        if cur_len>best_len:
            best_len = cur_len 
                
        return best_len

if __name__=="__main__":
    string = "pwwkew" # "abcabcbb"
    s = Solution()
    print(s.lengthOfLongestSubstring(string))