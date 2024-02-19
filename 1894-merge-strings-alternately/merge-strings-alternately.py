class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''

        length = min(len(word1),len(word2))
        for x in range(length):
            result+=word1[x]+word2[x]
        
        result += word1[length:]+word2[length:]

        return result             