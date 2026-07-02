class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        final=' '.join(words[:k])
        return final
        