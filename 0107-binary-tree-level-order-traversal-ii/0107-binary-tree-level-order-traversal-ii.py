# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans=[]
        def bfs(node):
            q=deque([node])

            while q:
                level=[]

                for _ in range(len(q)):
                    node=q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)

                ans.append(level)
            
            return ans
            
        output_rev=bfs(root)

        return output_rev[::-1]

        