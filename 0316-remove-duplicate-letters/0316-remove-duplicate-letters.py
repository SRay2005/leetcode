from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        remaining = Counter(s)
        stack = []
        visited = set()

        for ch in s:
            remaining[ch] -= 1

            if ch in visited:
                continue

            while (stack and ch < stack[-1] and remaining[stack[-1]] > 0):
                visited.remove(stack.pop()) #removes it from the stack as well as the visited set

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)