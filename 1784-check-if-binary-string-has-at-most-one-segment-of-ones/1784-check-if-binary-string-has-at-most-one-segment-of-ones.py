class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        ones=[i for i in s.split('0') if i]
        return len(ones)==1