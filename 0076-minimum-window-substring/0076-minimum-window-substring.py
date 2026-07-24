from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        ans = ""

        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1

            while all(need[c] <= 0 for c in need): #will be true when need count values of all keys in need will be <=0. 
                window = s[left:right+1] #we save this window

                if ans == "" or len(window) < len(ans): # we check if this is the first window, we save it as the ans, or if it is shorter than the current shortest window
                    ans = window

                if s[left] in need: #we shrink ny moving left pointer until the need values break the loop, and then expand  again using the right pointer due to the outer loop
                    need[s[left]] += 1
                left += 1

        return ans