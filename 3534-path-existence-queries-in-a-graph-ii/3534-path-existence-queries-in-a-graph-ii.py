from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # ---------------- Sort ----------------
        arr = sorted((nums[i], i) for i in range(n))

        values = [x for x, _ in arr]

        # original index -> sorted position
        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # ---------------- next[] ----------------
        # next[i] = furthest sorted index reachable in one edge
        nxt = [0] * n

        r = 0
        for l in range(n):
            r = max(r, l)
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            nxt[l] = r

        # ---------------- components ----------------
        comp = [0] * n
        cid = 0

        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # ---------------- binary lifting ----------------
        LOG = n.bit_length()

        up = [[0] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        # ---------------- answer queries ----------------
        ans = []

        for u, v in queries:

            l = pos[u]
            r = pos[v]

            if l > r:
                l, r = r, l

            if comp[l] != comp[r]:
                ans.append(-1)
                continue

            cur = l
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    jumps += 1 << k

            ans.append(jumps + 1 if l != r else 0)

        return ans