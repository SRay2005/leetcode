class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9 + 7
        binary=''
        for i in range(1, n+1):
            binary+=f"{i:b}"
        
        return int(binary, 2)%mod

        