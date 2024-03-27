class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        one=set()
        result=[]
        for x in nums1:
            if x not in nums2:
                one.add(x)
        two=set()
        for x in nums2:
            if x not in nums1:
                two.add(x)
        
        result.append(one)
        result.append(two)

        return result