class Solution:
    
    def merge_nodes(self , head : Optional[ListNode]) -> Optional[ListNode]:

        test = current = head
        current = current.next
        sum = 0

        while current:

            if current.val == 0:

                test = test.next
                test.val = sum
                sum = 0

            else : 

                sum = sum + current.val

            current = current.next

        test.next = None
        
        return head.next
