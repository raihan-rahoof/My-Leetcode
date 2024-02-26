class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            aliceMin = min(nums)
            nums.remove(aliceMin)
            bobMin = min(nums)
            nums.remove(bobMin)

            arr.append(bobMin)
            arr.append(aliceMin)

        return arr