class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True

        l=len(nums)
        i=0
        j=1
        while j<l:
            if (nums[i]%2==0 and nums[j]%2==1 )or (nums[i]%2==1 and nums[j]%2==0):
                i+=1
                j+=1
            else:
                return False
        
        return True
            