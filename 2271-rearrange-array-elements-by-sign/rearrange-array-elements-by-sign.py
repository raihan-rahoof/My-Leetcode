class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        minus = [x for x in nums if x<0 ]
        positive = [x for x in nums if x>0]

        result=[]
        while positive or minus:
            if positive:
                result.append(positive.pop(0))
            if minus:
                result.append(minus.pop(0))
        
        return result

