class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new = set()
        for x in nums:
            if x not in new:
                new.add(x)
            else:
                return x