class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adjacent={}
        output2=[]
        for i in range(n):
            adjacent[i]=set()
            output2.append(i)
        for x, y in invocations:
            adjacent[x].add(y)

        # infected={k}
        # change=True
        # while change:
        #     change=False
        #     for j in adjacent.keys():
        #         if j in infected:
        #             for i in adjacent[j]:
        #                 if i not in infected:
        #                     infected.add(i)
        #                     change=True

        infected = set()

        def dfs(node):
            infected.add(node)

            for nei in adjacent[node]:
                if nei not in infected:
                    dfs(nei)

        dfs(k)
        ans=[]
        for i in range(n):
            if i not in infected:
                if any(x in infected for x in adjacent[i]):
                    ans.append(i)
        
        if len(ans)==0:
            output=[]
            for i in range(0, n):
                if i not in infected:
                    output.append(i)
            
            return output
        
        else:
            return output2




