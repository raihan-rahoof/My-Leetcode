class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sp=s.split()
        result=" ".join(sp[:k])

        return result