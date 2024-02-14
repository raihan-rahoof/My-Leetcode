class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            rev=x[::-1]
            if rev == x:
                return x
        
        return ""