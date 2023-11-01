class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        num=sorted(list(set(nums)))
        if len(num)>2:
            return num[-3]
        else:
            return max(num)







        

        
            