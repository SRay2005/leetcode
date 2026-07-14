import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the number of ways to form subsequences with GCDs g1 and g2.
        # 0 acts as a placeholder for an empty subsequence.
        dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
        dp[0][0] = 1
        
        for x in nums:
            # We need a new DP table for the current step to avoid mutating state mid-loop
            next_dp = [[0] * (max_val + 1) for _ in range(max_val + 1)]
            
            for g1 in range(max_val + 1):
                for g2 in range(max_val + 1):
                    if dp[g1][g2] == 0:
                        continue
                        
                    v = dp[g1][g2]
                    
                    # Choice 1: Skip x (g1 and g2 stay the same)
                    next_dp[g1][g2] = (next_dp[g1][g2] + v) % MOD
                    
                    # Choice 2: Add x to seq1
                    ng1 = x if g1 == 0 else math.gcd(g1, x)
                    next_dp[ng1][g2] = (next_dp[ng1][g2] + v) % MOD
                    
                    # Choice 3: Add x to seq2
                    ng2 = x if g2 == 0 else math.gcd(g2, x)
                    next_dp[g1][ng2] = (next_dp[g1][ng2] + v) % MOD
                    
            dp = next_dp
            
        # Sum up all states where the two GCDs match and are not empty
        ans = 0
        for g in range(1, max_val + 1):
            ans = (ans + dp[g][g]) % MOD
            
        return ans