from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        output=''
        middle=''
        counts=Counter(s)
        sorted_counter = dict(sorted(counts.items()))
        
        for i in sorted_counter:
            if sorted_counter[i]//2>0:
                output+=i*(sorted_counter[i]//2)
                sorted_counter[i]%=2
                        
        if any(v > 0 for v in sorted_counter.values()):
            for i in sorted_counter:
                if sorted_counter[i]!=0:
                    middle+=i

        return output+middle+output[::-1]       
        