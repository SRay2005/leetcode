class Solution:
    def convert(self, s: str, numRows: int) -> str:
        dict1 = {i+1: "" for i in range(numRows)}    
        current=1
        direction=1
        final=''
        if numRows==1:
            return s
        for i in s:
            if current==1:
                direction=1
            elif current==numRows:
                direction=-1
            dict1[current]+=i
            current+=direction
        for i in dict1.values():
            final+=i
        return final
            
            

        
        