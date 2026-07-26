from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts=Counter(nums)
        total=0
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
                seen.add(k-i)
                if i!=k/2:
                    total+=min(counts[i], counts[k-i])
                else:
                    total+=counts[i]//2
                
        return total
        



        