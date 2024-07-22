class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}

        for x in arr:
            if x in count:
                count[x]+=1
            else:
                count[x]=1
        
        occurance={}
        for x in count.values():
            if x in occurance:
                return False
            occurance[x] =1
        return True
        
        