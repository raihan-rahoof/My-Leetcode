class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one=[]
        result=[]
        for x in nums1:
            if x not in nums2:
                if x not in one:
                   one.append(x)
        two=[]
        for x in nums2:
            if x not in nums1:
                if x not in two:
                    two.append(x)
        
        result.append(one)
        result.append(two)

        return result