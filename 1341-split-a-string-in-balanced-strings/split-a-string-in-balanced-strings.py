class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count =0
        balance = 0

        for x in s:
            if x == 'R':
                balance +=1
            else:
                balance -=1
            
            if balance == 0:
                count+=1
        
        return count
