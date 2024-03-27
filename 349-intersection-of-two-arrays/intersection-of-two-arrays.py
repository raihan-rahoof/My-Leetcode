class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new = []
        for x in nums1:
            if x in nums2:
                if x not in new:
                    new.append(x)
        
        return new