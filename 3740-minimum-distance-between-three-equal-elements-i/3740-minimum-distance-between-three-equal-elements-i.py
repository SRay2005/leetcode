class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        unique=set(nums)
        possible=[]
        for i in unique:
            if nums.count(i)>=3:
                possible.append(i)
        
        dict1={}
        for i in possible:
            dict1[i]=[]
            for j in range(n):
                if nums[j]==i:
                    dict1[i].append(j)

        if len(dict1)==0:
            return -1        
        min_dist=float('inf')
        for p in dict1.values():
            for i in range(len(p) - 2):
                triplet = p[i : i+3]
                x,y,z=triplet
                if  abs(x - y) + abs(y - z) + abs(z - x)<min_dist:
                    min_dist=abs(x - y) + abs(y - z) + abs(z - x)
            
        return min_dist

        