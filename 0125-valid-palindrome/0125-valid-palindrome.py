class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned=''.join(c for c in s if c.isalnum()).lower()
        
        if cleaned==cleaned[::-1]:
            return True
        else:
            return False