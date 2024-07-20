from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)

        count_b=char_count['b']
        count_a=char_count['a']
        count_l=char_count['l']//2
        count_o=char_count['o']//2
        count_n=char_count['n']

        return min(count_b,count_a,count_l,count_o,count_n)

        
