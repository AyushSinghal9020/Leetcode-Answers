# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next

        if count == 1 : return None    
            
        temp = head
        count = count - n +1

        if count == 1 : return head.next

        while (count -2 ):
            
            temp = temp.next
            count -= 1
          
        if n == 1 : temp.next = None
        else : temp.next = temp.next.next        

        return head
