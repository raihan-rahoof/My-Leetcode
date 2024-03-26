class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = [x**2 for x in nums]
        new.sort()
        return new