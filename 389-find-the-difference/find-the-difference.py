class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) > len(t):
            for x in s:
                if s.count(x) > t.count(x):
                    return x
                    break
        if len(t) > len(s):
            for x in t:
                if t.count(x) > s.count(x):
                    return x
                    break