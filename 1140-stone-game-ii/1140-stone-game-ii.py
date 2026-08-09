class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        dp = {}

        def solve(i, M):
            # No piles left
            if i == n:
                return 0

            # Can take everything remaining
            if 2 * M >= n - i:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            # Try taking X piles
            for X in range(1, 2 * M + 1):
                # Stones we take
                taken = suffix[i] - suffix[i + X]

                # Opponent's best score from the remaining piles
                opponent = solve(i + X, max(M, X))

                # We want to maximize our final score
                best = max(best, taken + suffix[i + X] - opponent)

            dp[(i, M)] = best
            return best

        return solve(0, 1)