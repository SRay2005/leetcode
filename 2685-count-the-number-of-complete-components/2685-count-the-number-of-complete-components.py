from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        # Step 1: Build the adjacency list graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        complete_components_count = 0
        
        # Step 2: Loop through every node from 0 to n-1 
        # (This catches disconnected islands!)
        for i in range(n):
            if i not in visited:
                # We found a new island! Let's gather all its members
                island_nodes = []
                
                # Standard DFS to explore the entire current island
                def dfs(node):
                    visited.add(node)
                    island_nodes.append(node)
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            dfs(neighbor)
                
                dfs(i)
                
                # Step 3: Verify if this island is "Complete"
                num_nodes = len(island_nodes)
                is_complete = True
                
                # Check if every member has exactly (num_nodes - 1) neighbors
                for node in island_nodes:
                    if len(graph[node]) != num_nodes - 1:
                        is_complete = False
                        break # One broken link ruins the whole complete component
                
                if is_complete:
                    complete_components_count += 1
                    
        return complete_components_count