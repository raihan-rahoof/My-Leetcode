class Solution:
    def romanToInt(self, s: str) -> int:
        romandict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    
        result = 0
        prevalue = 0
        
        for c in s[::-1]:
            value = romandict[c]
            if value < prevalue:
                result -= value
            else:
                result += value
            prevalue = value
        
        return result

        
