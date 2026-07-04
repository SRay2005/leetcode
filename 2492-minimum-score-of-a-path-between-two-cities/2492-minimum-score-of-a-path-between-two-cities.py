class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        shortest=100001
        nodes_to_1={1}
        roads.sort()
        changed = True
        while changed:
            changed = False
            for i in roads:
                if i[0] in nodes_to_1 or i[1] in nodes_to_1:
                    before = len(nodes_to_1)
                    nodes_to_1.add(i[0])
                    nodes_to_1.add(i[1])
                    if len(nodes_to_1) > before:
                        changed = True
        for i in roads:
            if (i[2]<shortest) and ((i[0] in nodes_to_1) or (i[1] in nodes_to_1)):
                shortest=i[2]
        return shortest
        


        

