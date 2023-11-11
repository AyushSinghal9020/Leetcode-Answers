# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value
        
        l_list = iter_link(head)

        def pair_swapper(li):

            index_1 = 0
            index_2 = 1

            while index_2 < len(li):

                li[index_1] , li[index_2] = li[index_2] , li[index_1]

                index_1 += 2
                index_2 += 2 

            return li

        rt = pair_swapper(l_list)

        dummy_head = ListNode(0)
        tail = dummy_head

        for val in rt:

            new_node = ListNode(int(val))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result
