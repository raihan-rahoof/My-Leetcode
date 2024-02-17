class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        scores=[]
        for x in grid:
            scores.append(sum(x))
        
        return scores.index(max(scores))