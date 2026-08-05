"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return 
        
        q=deque([root])

        while q:
            level=[]
            sz = len(q)
            for _ in range(sz):
                node=q.popleft()
                level.append(node)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            for i in range(len(level)-1):
                level[i].next = level[i+1]
        
        return root
    

        

