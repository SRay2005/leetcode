class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        count=0
        seen=set()
        m=0
        for i in word:
            if i not in seen:
                seen.add(i)
                m+=1
        
        factor=1
        while m>0:
            count+=(min(m,8))*factor
            m=m-8
            factor+=1

        return count



        