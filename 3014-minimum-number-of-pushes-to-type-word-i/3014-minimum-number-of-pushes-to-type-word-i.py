class Solution:
    def minimumPushes(self, word: str) -> int:
        m=len(word)
        count=0
        factor=1
        while m>0:
            count+=(min(m,8))*factor
            m=m-8
            factor+=1

        return count



        