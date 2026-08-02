# from functools import lru_cache
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         @lru_cache(None)
#         def max_diff(left, right):
#             if left==right:
#                 return piles[left]
#             pick_left=piles[0]-max_diff(left+1, right)
#             pick_right=piles[-1]-max_diff(left, right-1)      

#             return max(pick_left, pick_right)  
        
#         return max_diff(0, len(piles) - 1) >= 0


    #since there are an even number of piles, alice will always win

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True