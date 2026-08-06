# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements=[-1]*10001

        def dfs(node):
            nonlocal elements
            if node is None:
                return
            
            elements[node.val]+=1

            if node.left:
                dfs(node.left)
            
            if node.right:
                dfs(node.right)
            

            
        dfs(root)
        n=len(elements)
        for i in range(n):
            if k==1 and elements[i]>-1:
                return i

            if elements[i]>-1:
                k-=1
        


        
                