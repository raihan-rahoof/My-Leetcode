class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=len(nums)
        for x in range(0,l):
            for y in range(x+1,l):
                if nums[x]+nums[y]==target:
                    return x , y
