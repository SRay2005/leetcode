class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m=len(boxGrid)
        n=len(boxGrid[0])
        rotated = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                rotated[i][j] = boxGrid[j][i]

        for i in range(n):
            rotated[i].reverse()

         # OPTIMIZED GRAVITY: Process each column (j) from bottom to top
        for j in range(m):
            empty = n - 1  # Track the lowest available row in this column
            
            for i in range(n - 1, -1, -1):
                if rotated[i][j] == '*':
                    # Obstacle found: stones can only land above it now
                    empty = i - 1
                elif rotated[i][j] == '#':
                    # Stone found: drop it straight down to the lowest empty spot
                    if empty > i:
                        rotated[empty][j] = '#'
                        rotated[i][j] = '.'
                    # Move the empty tracker up by 1 row
                    empty -= 1
        
        return rotated


# my bruteforce approach

# change=True
#         while change:
#             change=False
#             for i in range(n-1, 0, -1):
#                 for j in range(m-1, -1, -1):
#                     if rotated[i][j]=='.' and rotated[i-1][j]=='#':
#                         rotated[i][j], rotated[i-1][j] = rotated[i-1][j], rotated[i][j]
#                         change=True
        
#         return rotated