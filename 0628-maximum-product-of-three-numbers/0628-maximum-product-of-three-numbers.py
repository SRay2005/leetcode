class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest=float("-inf")
        second=float("-inf")
        third=float("-inf")
        minm=float("inf")
        secondmin=float("inf")
        for i in nums:
            if i>largest:
                third=second
                second=largest
                largest=i
            elif largest>=i>second:
                third=second
                second=i
            elif second>=i>third:
                third=i
        
        for i in nums:
            if i<=minm:
                secondmin=minm
                minm=i
            elif secondmin>i>=minm:
                secondmin=i
        return max(largest*second*third, largest*minm*secondmin)



        