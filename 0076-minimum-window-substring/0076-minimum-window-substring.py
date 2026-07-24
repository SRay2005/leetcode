from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        left = 0
        ans = ""

        for right in range(len(s)):
            if s[right] in need:
                need[s[right]] -= 1

            while all(need[c] <= 0 for c in need):
                window = s[left:right+1]

                if ans == "" or len(window) < len(ans):
                    ans = window

                if s[left] in need:
                    need[s[left]] += 1
                left += 1

        return ans