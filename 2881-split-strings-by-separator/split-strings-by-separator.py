class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = [x.split(separator) for x in words]
        res=[]
        for x in ans:
            for y in x:
                if y:
                    res.append(y)
        return res
