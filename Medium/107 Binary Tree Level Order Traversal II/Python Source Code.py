# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        rt = {}

        def recur(root , level) : 

            if root : 

                recur(root.left , level + 1)

                if level in rt.keys() : rt[level].append(root.val)
                else : rt[level] = [root.val]

                recur(root.right , level + 1)

        recur(root , 0)

        ret = sorted(rt.keys())
        rt = [
            rt[val]
            for val 
            in ret
        ]

        return rt[::-1]
        
