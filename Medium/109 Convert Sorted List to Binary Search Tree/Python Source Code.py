# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]: 

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value 

        lis = iter_link(head)
        
        def to_tree(nums) : 

            total_nums = len(nums)
            
            if not total_nums : return None

            mid_node = total_nums // 2
            return TreeNode(
                nums[mid_node], 
                to_tree(nums[:mid_node]) , 
                to_tree(nums[mid_node + 1 :])
            )

        return to_tree(lis)
