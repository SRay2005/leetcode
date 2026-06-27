class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1=False
        z2=False
        for i in range(len(nums1)):
            if nums1[i]==0:
                nums1[i]=1
                z1=True
        
        for i in range(len(nums2)):
            if nums2[i]==0:
                nums2[i]=1
                z2=True
        s1=sum(nums1)
        s2=sum(nums2)
        if s1==s2:
            return s1
        elif s1>s2 and z2:
            return s1
        elif s2>s1 and z1:
            return s2
        return -1



