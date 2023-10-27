class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        dif=arr[1]-arr[0]

        for x in range(1,len(arr)):
            if arr[x]-arr[x-1]!=dif:
                return False
        
        return True

            