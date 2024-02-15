class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = [x for x in nums if nums.count(x)==1]
        return ans[0]