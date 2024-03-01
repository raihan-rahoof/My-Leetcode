class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        num = sum(1 for x in hours if x >= target)
        return num