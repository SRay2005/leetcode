class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int):
        n = len(customers)
        max_mins = -1
        start_max_mins = -1
        total = 0

        for i in range(n - minutes + 1):
            m = sum(customers[j] for j in range(i, i + minutes)
                    if grumpy[j] == 1)

            if m > max_mins:
                max_mins = m
                start_max_mins = i

        for x in range(start_max_mins, start_max_mins + minutes):
            grumpy[x] = 0

        for p in range(n):
            if grumpy[p] == 0:
                total += customers[p]

        return total