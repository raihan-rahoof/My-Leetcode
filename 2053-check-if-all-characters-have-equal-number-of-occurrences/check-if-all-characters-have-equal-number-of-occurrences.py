class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dick = dict()
        for x in s:
            if x not in dick:
                dick[x]=0
            dick[x]+=1
        
        li=[x for x in dick.values()]
        first=li[0]
        for x in li[1:]:
            if first!=x:
                return False
            
        return True
