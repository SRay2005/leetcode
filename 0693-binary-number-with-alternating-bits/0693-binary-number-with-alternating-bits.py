class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary=f"{n:b}"
        if '00' in binary or '11' in binary:
            return False
        
        return True
        