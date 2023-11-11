# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value 

        l_list1 = iter_link(list1)
        l_list2 = iter_link(list2)

        l_list = sorted(l_list1 + l_list2)

        dummy_head = ListNode(0)
        tail = dummy_head

        for val in l_list:

            new_node = ListNode(int(val))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result
