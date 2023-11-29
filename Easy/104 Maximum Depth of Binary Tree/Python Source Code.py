# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        rt = []

        def recur(root , level) : 

            if root : 

                recur(root.left , level + 1)

                rt.append(level)

                recur(root.right , level + 1)

        recur(root , 1)

        if rt != [] : return max(rt)
        return 0
