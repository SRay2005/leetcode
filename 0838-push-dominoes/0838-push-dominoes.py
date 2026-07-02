class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        arr = list(dominoes)
        n = len(arr)

        # Indices of the last and current non-dot domino
        left = -1
        left_force = 'L'

        for right in range(n + 1):
            if right == n:
                right_force = 'R'
            elif arr[right] == '.':
                continue
            else:
                right_force = arr[right]

            if left_force == right_force:
                # L...L or R...R
                for k in range(left + 1, right):
                    arr[k] = left_force

            elif left_force == 'R' and right_force == 'L':
                # R...L
                l, r = left + 1, right - 1
                while l < r:
                    arr[l] = 'R'
                    arr[r] = 'L'
                    l += 1
                    r -= 1
                # If l == r, leave the middle domino as '.'

            # L...R -> do nothing

            left = right
            left_force = right_force

        return "".join(arr)