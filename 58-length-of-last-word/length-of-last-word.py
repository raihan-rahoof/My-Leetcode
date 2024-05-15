class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new = s.split()
        word = new.pop()

        return len(word)