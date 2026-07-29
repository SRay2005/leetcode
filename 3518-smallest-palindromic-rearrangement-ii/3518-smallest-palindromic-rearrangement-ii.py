from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:

        # ----------------------------------------------------------
        # Count frequency of every character.
        # ----------------------------------------------------------
        freq = Counter(s)

        # Middle character (if string length is odd)
        mid = ""

        # half[i] = occurrences of character i
        # needed in the first half of the palindrome.
        #
        # Example:
        # "aaabbbb"
        #
        # half:
        # a -> 1
        # b -> 2
        #
        # because the second half is automatically determined.
        half = [0] * 26

        for ch, cnt in freq.items():
            if cnt % 2:
                mid = ch
            half[ord(ch) - ord('a')] = cnt // 2

        # Total length of first half.
        m = sum(half)

        # ----------------------------------------------------------
        # Precompute factorials.
        # Needed only ONCE to calculate the initial number
        # of distinct permutations.
        # ----------------------------------------------------------
        fact = [1] * (m + 1)

        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        # ----------------------------------------------------------
        # Calculate total distinct permutations of the multiset.
        #
        # Formula:
        #
        # total!
        # --------------------
        # c1! c2! c3! ...
        # ----------------------------------------------------------
        ways = fact[m]

        for cnt in half:
            ways //= fact[cnt]

        # If kth permutation doesn't exist.
        if k > ways:
            return ""

        answer = []

        # Remaining positions still to be filled.
        remaining = m

        # ----------------------------------------------------------
        # Build the first half greedily.
        #
        # At every position:
        #
        # Try 'a'
        # Try 'b'
        # ...
        #
        # Count how many permutations begin with that character.
        #
        # If that block contains the kth permutation,
        # choose it.
        #
        # Otherwise skip the entire block.
        # ----------------------------------------------------------
        while remaining:

            for ch in range(26):

                if half[ch] == 0:
                    continue

                # --------------------------------------------------
                # Number of permutations if we place this character.
                #
                # Instead of recomputing:
                #
                # (remaining-1)! / ...
                #
                # we use
                #
                # newWays = ways * freq / remaining
                #
                # Derived from:
                #
                # L! / c!
                # ----------------
                # (L-1)!/(c-1)!
                #
                # = remaining / freq
                # --------------------------------------------------
                newWays = ways * half[ch] // remaining

                # ----------------------------------------------
                # kth permutation lies inside this block.
                # Permanently choose this character.
                # ----------------------------------------------
                if newWays >= k:

                    answer.append(chr(ch + ord('a')))

                    # Update the current permutation count.
                    ways = newWays

                    # One copy of this character has been used.
                    half[ch] -= 1

                    remaining -= 1

                    break

                # ----------------------------------------------
                # Skip every permutation beginning with this
                # character.
                # ----------------------------------------------
                else:
                    k -= newWays

        left = "".join(answer)

        return left + mid + left[::-1]