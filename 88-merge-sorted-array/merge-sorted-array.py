class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        a = len(nums1)-m
        for x in range(a):
            nums1.remove(nums1[-1])
        
        b = len(nums2)-n
        for x in range(b):
            nums2.remove(nums2[-1])
        
        nums1.extend(nums2)
        nums1.sort()
       

        
        


        