class Solution:
    def binaryGap(self, n: int) -> int:
        greatest=0
        current=0
        binary=f"{n:b}"
        for i in range(0, len(binary)):
            if binary[i]=='1':
                if i-current>greatest:
                    greatest=i-current
                current=i
        return greatest
            

        