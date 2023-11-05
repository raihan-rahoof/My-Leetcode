class Solution:
    def hammingWeight(self, n: int) -> int:
        num=bin(n)

        return num.count("1")