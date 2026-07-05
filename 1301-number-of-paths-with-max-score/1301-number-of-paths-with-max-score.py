class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        # score[i][j] = maximum score to reach (i,j) from S
        # -1 means this cell is unreachable
        score = [[-1] * n for _ in range(n)] #creates a n by n matrix of -1
        # ways[i][j] = number of ways to achieve score[i][j]
        ways = [[0] * n for _ in range(n)]
        # Base case: Start at S
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1
        # Traverse from bottom-right to top-left
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Skip obstacles
                if board[i][j] == 'X':
                    continue
                # Skip S since we've already initialized it
                if i == n - 1 and j == n - 1:
                    continue
                # Look at the three cells we could have come from
                neighbours = []
                if i + 1 < n:
                    neighbours.append((i + 1, j))
                if j + 1 < n:
                    neighbours.append((i, j + 1))
                if i + 1 < n and j + 1 < n:
                    neighbours.append((i + 1, j + 1))
                # Find the best score among reachable neighbours
                best = -1
                for x, y in neighbours:
                    best = max(best, score[x][y])
                # If no neighbour is reachable, this cell is unreachable
                if best == -1:
                    continue
                # Count all ways that achieve the best score
                totalWays = 0
                for x, y in neighbours:
                    if score[x][y] == best:
                        totalWays = (totalWays + ways[x][y]) % MOD
                # Current cell's value
                if board[i][j] in ('S', 'E'):
                    value = 0
                else:
                    value = int(board[i][j])
                score[i][j] = best + value
                ways[i][j] = totalWays
        # If E is unreachable
        if ways[0][0] == 0:
            return [0, 0]
        return [score[0][0], ways[0][0]]