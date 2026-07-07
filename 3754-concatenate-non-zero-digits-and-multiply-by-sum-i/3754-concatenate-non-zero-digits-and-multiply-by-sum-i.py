class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        x=0
        number=0
        multiplier=1
        while n:
            x=n%10
            n=n//10

            if x!=0:
                number += multiplier * x
                sum+=x
                multiplier*=10
        
        return sum*number