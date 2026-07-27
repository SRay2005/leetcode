class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxm=-1
        second=-1
        for i in nums:
            if i>=maxm:
                second=maxm
                maxm=i
            elif maxm>i>second:
                second=i

        return (second-1)*(maxm-1)
            
        