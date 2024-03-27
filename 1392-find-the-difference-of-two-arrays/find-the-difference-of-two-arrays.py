class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one = set(nums1)
        two = set(nums2)

        r1 = [x for x in one if x not in two]
        r2 = [x for x in two if x not in one]

        return [r1,r2]