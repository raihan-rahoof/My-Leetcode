class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]
        for x in range(len(nums)):
            target.insert(index[x],nums[x])
        
        return target