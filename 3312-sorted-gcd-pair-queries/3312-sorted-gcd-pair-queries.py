from typing import List
from itertools import accumulate
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Optimize by only going up to the actual maximum number in nums
        max_num = max(nums)
        
        # 1. Count frequencies of each number
        cnt = [0] * (max_num + 1)
        for x in nums:
            cnt[x] += 1
            
        # 2. Count pairs with GCD exactly 'g'
        pairs_with_gcd = [0] * (max_num + 1)
        
        # Iterate backwards to use inclusion-exclusion
        for g in range(max_num, 0, -1):
            # Fast C-level slicing to count multiples of g
            multiples_count = sum(cnt[g::g])
            
            # Total pairs where both elements are multiples of g
            total_pairs = multiples_count * (multiples_count - 1) // 2
            
            # Fast C-level slicing to subtract pairs where GCD is a higher multiple of g
            # cnt[2*g::g] starts at 2*g and goes up by steps of g
            total_pairs -= sum(pairs_with_gcd[2*g::g])
            
            pairs_with_gcd[g] = total_pairs
            
        # 3. Create prefix sums using the highly-optimized accumulate function
        prefix_sums = list(accumulate(pairs_with_gcd))
            
        # 4. Answer queries using binary search via list comprehension
        return [bisect_left(prefix_sums, q + 1) for q in queries]