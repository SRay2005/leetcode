class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        r=len(grid)
        c=len(grid[0])

        score = [[float('inf')]* c for _ in range(r)]

        score[0][0]=grid[0][0]

        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    continue
                neighbors=[]
                if i>0:
                    neighbors.append((i-1, j))
                if j>0:
                    neighbors.append((i, j-1))
                minimum=float('inf')
                for x,y in neighbors:
                    minimum=min(minimum, score[x][y])
                value = grid[i][j]
                score[i][j]=minimum+value
        return score[r-1][c-1]



        