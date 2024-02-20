class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dick=dict()
        dick2= dict()
        for x in range(len(nums1)):
            if nums1[x] in nums2:
                if x not in dick:
                    dick[x] = 1
                else:
                    dick[x] += 1

        for x in range(len(nums2)):
            if nums2[x] in nums1:
                if x not in dick2:
                    dick2[x] = 1
                else:
                    dick2[x] += 1


        result = [sum(dick.values()),sum(dick2.values())]
        return result