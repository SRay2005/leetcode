class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words=s.split()
        final=''
        for i in range(0, k):
            final+=words[i]
            final+=' '
        return final[:-1]
        