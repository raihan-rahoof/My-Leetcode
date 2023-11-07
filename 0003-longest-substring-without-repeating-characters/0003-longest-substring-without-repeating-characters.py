class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)== 0:
            return 0
        
        i , j , max_len = 0,0,0
        check = set()

        while j < len(s):
            if s[j] not in check:
                check.add(s[j])
                max_len = max(max_len , j-i+1)
                j+=1
            else:
                check.remove(s[i])
                i+=1
        
        return max_len
