class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(s)

        # powers of 10
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD

        sumD = [0] * (n + 1)
        cntN0 = [0] * (n + 1)
        p = [0] * (n + 1)

        for i, ch in enumerate(s, 1):
            d = ord(ch) - 48                # converts a digit character ('0'–'9') into its integer value.

            sumD[i] = sumD[i - 1] + d
            cntN0[i] = cntN0[i - 1] + (d != 0) # we can use bool with integers to add 1 if the condition is met

            if d:
                p[i] = (p[i - 1] * 10 + d) % MOD
            else:
                p[i] = p[i - 1]

        ans = []

        for l, r in queries:        #building the number
            k = cntN0[r + 1] - cntN0[l]
            digitSum = sumD[r + 1] - sumD[l]

            x = (p[r + 1] - p[l] * pow10[k]) % MOD

            ans.append(x * digitSum % MOD)

        return ans