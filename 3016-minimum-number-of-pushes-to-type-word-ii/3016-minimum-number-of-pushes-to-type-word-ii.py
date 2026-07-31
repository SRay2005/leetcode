from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        counts=Counter(word)
        sorteddict = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
        count=0
        output=0
        factor=1
        for i in sorteddict.values():
            if count==8:
                factor+=1
                count=0
            
            output+=(factor*i)
            count+=1

        return output
