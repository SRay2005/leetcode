import math

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        # sum_odd=n*n
        # sum_even=n*(n+1)
        # return gcd(sum_even, sum_odd)
         

#gcd(n, n + 1) = 1, so this just simplifies to gcd(n^2, n^2+n) = n*gcd(n, n+1) = n