class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dick = dict()
        for x in s:
            if x not in dick:
                dick[x]=0
            dick[x]+=1
        
        
        
            
        return len(set(dick.values()))==1
