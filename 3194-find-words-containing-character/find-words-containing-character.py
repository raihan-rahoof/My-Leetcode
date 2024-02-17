class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result=[]
        for i,w in enumerate(words):
            if x in w:
                result.append(i)
                
        
        return result