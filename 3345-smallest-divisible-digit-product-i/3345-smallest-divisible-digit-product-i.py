class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product=1
            copied=n
            while copied:
                product*=(copied%10)
                copied=copied//10
            
            if product%t==0:
                return n
            
            n+=1
        


        