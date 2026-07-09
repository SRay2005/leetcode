class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[bool]:
        # Array to store which component/group each index belongs to
        group = [0] * n
        curr_group = 0
        
        # Linear sweep to identify "walls" and mark separate components
        for i in range(1, n):
            # If the difference between adjacent elements exceeds maxDiff,
            # we must start a brand new connected component.
            if nums[i] - nums[i-1] > maxDiff:
                curr_group += 1
            group[i] = curr_group
            
        # Answer each query instantly in O(1) time by checking group equality
        return [group[u] == group[v] for u, v in queries]