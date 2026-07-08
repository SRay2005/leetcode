class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        n = len(mat)
        
        # Track if each of the 4 rotation states is still valid
        r0, r90, r180, r270 = True, True, True, True
        
        for i in range(n):
            for j in range(n):
                # 0 degree match
                if mat[i][j] != target[i][j]:
                    r0 = False
                # 90 degree clockwise match
                if mat[n - 1 - j][i] != target[i][j]:
                    r90 = False
                # 180 degree match
                if mat[n - 1 - i][n - 1 - j] != target[i][j]:
                    r180 = False
                # 270 degree clockwise match
                if mat[j][n - 1 - i] != target[i][j]:
                    r270 = False
                    
        # If any global rotation state is completely valid, return True
        return r0 or r90 or r180 or r270
