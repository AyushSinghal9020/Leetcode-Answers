# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value

        last_list = []

        for val in lists : 
            
            links = iter_link(val)

            last_list += links

        last_list = sorted(last_list)

        dummy_head = ListNode(0)
        tail = dummy_head

        for val in last_list:

            new_node = ListNode(int(val))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result
