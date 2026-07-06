class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort()
        for i in range(n):
            for j in range(i+1, n):
                if (intervals[i][0]<=intervals[j][0] and intervals[i][1] >= intervals[j][1]) :
                    intervals[j]=intervals[i]
                    
                elif (intervals[j][0]<=intervals[i][0] and intervals[j][1] >= intervals[i][1]):
                    intervals[i]=intervals[j]
                    
        seen=set()
        count=0
        for x,y in intervals:
            if (x,y) not in seen:
                count+=1
            seen.add((x,y))
        return count

        