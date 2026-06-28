class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0]=1
        n=len(arr)
        check=0
        for i in range(n):
            if abs(arr[i]-check)>1:
                arr[i]=check+1
            check=arr[i]
        return max(arr)
                

            


        