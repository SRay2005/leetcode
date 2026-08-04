class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing=[]
        setnums=set(nums)
        highest=max(nums)
        lowest=min(nums)
        for i in range(lowest, highest):
            if i not in setnums:
                missing.append(i)


        return missing        