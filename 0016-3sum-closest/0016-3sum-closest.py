class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        smallest=float('inf')
        closest=None
        i=0
        for i in range(n):
            left=i+1
            right=n-1
            while left<right:
                if abs((nums[left]+nums[right])-(target-nums[i]))<smallest:
                    smallest=abs((nums[left]+nums[right])-(target-nums[i]))
                    closest=(nums[left]+nums[right]+nums[i])

                if nums[left]+nums[right]>target-nums[i]:
                    right-=1
                    continue

                if nums[left]+nums[right]<target-nums[i]:
                    left+=1
                    continue
                
                if nums[left]+nums[right]==target-nums[i]:
                    return nums[left]+nums[right]+nums[i]

        return closest