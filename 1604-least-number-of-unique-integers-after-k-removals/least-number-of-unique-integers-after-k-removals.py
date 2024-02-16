class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = dict()
        for x in arr:
            if x not in freq:
                freq[x]=0
            
            freq[x]+=1

        l=list(freq.values())
        l.sort()
        for x in range(len(l)):
            if l[x] <= k:
                k-=l[x]
                l[x]=-1
            else:
                break
        
        num=l.count(-1)
        
        return len(l)-num
        