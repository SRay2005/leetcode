class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        substrings = {}
        ans = []

        # Generate all unique substrings for each string
        for i in range(n):
            arrlen = len(arr[i])
            subs = set()

            for j in range(arrlen):
                for z in range(j, arrlen):  
                    subs.add(arr[i][j:z + 1])

            substrings[i] = subs   # use index instead of string

        # Find shortest unique substring
        for i in range(n):
            curr = None

            for sub in substrings[i]:   # iterate over the set
                count = 0

                for s in arr:
                    if sub in s:
                        count += 1

                if count == 1:
                    if (
                        curr is None
                        or len(sub) < len(curr)
                        or (len(sub) == len(curr) and sub < curr)
                    ):
                        curr = sub

            ans.append("" if curr is None else curr)

        return ans