class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        test=[]
        for x in words:
            if x in test or x[::-1] in test:
                count+=1
            else:
                test.append(x)
        return count
