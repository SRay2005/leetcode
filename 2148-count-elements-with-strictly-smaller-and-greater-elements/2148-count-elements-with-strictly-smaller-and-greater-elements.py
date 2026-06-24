class Solution:
    def countElements(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i == max(nums) or i== min(nums):
                continue
            count+=1
        return count