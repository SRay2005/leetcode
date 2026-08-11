class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        total=[]
        n=len(nums)
        i=1
        while i<=n:
            seen_right=set()
            seen_left=set()
            count=0
            for x in range(i, n):
                if nums[x] not in seen_right:
                    seen_right.add(nums[x])
                    count-=1
                
            for x in range(0, i):
                if nums[x] not in seen_left:
                    seen_left.add(nums[x])
                    count+=1

                    
            total.append(count)
            i+=1
        
        return total




        