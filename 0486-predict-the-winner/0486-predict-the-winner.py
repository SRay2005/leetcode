from functools import lru_cache #used for memoization

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def max_diff(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            # Pick left: gain nums[left], opponent gets max_diff(left+1, right)
            pick_left = nums[left] - max_diff(left + 1, right)
            
            # Pick right: gain nums[right], opponent gets max_diff(left, right-1)
            pick_right = nums[right] - max_diff(left, right - 1)
            
            return max(pick_left, pick_right)

        return max_diff(0, len(nums) - 1) >= 0   