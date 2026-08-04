class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer=[]
        n=len(nums)
        nums.sort()
        present=set()
        for i in range(n):
            for j in range(i+1, n):
                left=j+1
                right=n-1
                while left<right:
                    total=nums[i]+nums[j]+nums[left]+nums[right]
                    if total<target:
                        left+=1
                        continue
                    
                    if total>target:
                        right-=1
                        continue

                    if total==target:
                        if (nums[i], nums[j], nums[left], nums[right]) not in present:
                            answer.append([nums[i], nums[j], nums[left], nums[right]])
                            present.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
        
        return answer


