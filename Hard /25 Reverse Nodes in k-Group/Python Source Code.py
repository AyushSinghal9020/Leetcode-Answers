# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value 

        l_list = iter_link(head)

        list_breaker = lambda li , n : [
            li[index : index + n]
            for index 
            in range(0 , len(li) , n)
        ]

        def n_swapper(li , n) : 

            n_lists = list_breaker(li , n)

            for val in n_lists:

                if len(val) == n: val.reverse()

            rt = []

            for val in n_lists:
                
                for value in val : rt.append(value)

            return rt

        rt = n_swapper(l_list , k)

        dummy_head = ListNode(0)
        tail = dummy_head

        for val in rt:

            new_node = ListNode(int(val))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result   
