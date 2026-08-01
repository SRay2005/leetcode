class Solution:
    def countDigitOne(self, n: int) -> int:
        factor = 1
        ans=0
        while factor <= n:
            lower = n % factor
            current = (n // factor) % 10
            higher = n // (factor * 10)

            if current == 0:
                ans += higher * factor
            elif current == 1:
                ans += higher * factor + lower + 1
            else:
                ans += (higher + 1) * factor

            factor *= 10
        
        return ans