class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        n=len(words)
        total=n
        removed=set()
        for word in words:
            total+=len(word)
        for i in range(n):
            for j in range(i+1, n):
                if words[j] not in removed and (words[j]==words[i][-(len(words[j])):]):
                    total-=(len(words[j])+1)
                    removed.add(words[j])
                elif words[i] not in removed and (words[i] in words[j][-(len(words[i])):]):
                    total-=(len(words[i])+1)
                    removed.add(words[i])

        return total
        