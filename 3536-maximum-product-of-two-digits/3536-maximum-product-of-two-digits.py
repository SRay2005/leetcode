class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        largest=-1
        second=-1
        for i in s:
            if int(i)>largest:
                second=largest
                largest=int(i)
            elif largest >= int(i) > second:
                second=int(i)
        return largest*second

        