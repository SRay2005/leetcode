class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        c=[]
        for i in range(len(A)):
            count=0
            for j in A[:i+1]:
                if j in B[:i+1]:
                    count+=1
            c.append(count)
        return c

        