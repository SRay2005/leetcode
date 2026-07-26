import math
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        total=0
        for i in range(n):
            if f'{i:b}'.count('1')==k:
                total+=nums[i]

        return total
        