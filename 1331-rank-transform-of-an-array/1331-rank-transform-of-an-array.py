from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dict1=defaultdict(int)
        rank=1
        seen=set()
        temp=arr.copy()
        temp.sort()
        n=len(arr)
        for i in temp:
            if i not in seen:
                seen.add(i)
                dict1[i]=rank
                rank+=1
        for i in range(n):
            arr[i]=dict1[arr[i]]
        
        return arr

        
        
            

        


        