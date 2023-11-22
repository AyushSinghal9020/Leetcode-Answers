# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value 

        val = iter_link(head)

        if val != []:

            for _ in range(k % len(val)) : val.insert(0 , val.pop(-1))

        dummy_head = ListNode(0)
        tail = dummy_head

        for value in val:

            new_node = ListNode(int(value))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result
