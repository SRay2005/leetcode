class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a=0
        b=0
        l=0
        n=0
        o=0
        for i in text:
            if i=='a':
                a+=1
            elif i=='b':
                b+=1
            elif i=='l':
                l+=1
            elif i=='n':
                n+=1
            elif i=='o':
                o+=1
        return min(a,b,l//2,n,o//2)