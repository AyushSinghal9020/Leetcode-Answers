# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# <---------METHOD 1--------->

class Solution:
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        dummy = slow = fast = ListNode(-math.inf)
        dummy.next = head
        
        while fast.next and fast.next.next:
            
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next    
        
        return dummy.next

# <---------METHOD 2--------->

class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def link_iter(node):

            sample_node = node
            link_list = []

            while sample_node : 
                link_list.append(sample_node.val)
                sample_node = sample_node.next

            return link_list

        link_list = link_iter(head)

        if len(link_list) == 1 : return None
        if len(link_list) == 2 :
            
            head.next = None
            
            return head
        
        if len(link_list) == 3 :
            
            head.next = head.next.next
            
            return head
        
        middle = round((len(link_list) - 1) / 2)
        
        counter = 0
        sample_head = head

        while sample_head:

            sample_head = sample_head.next
            counter += 1

            if counter == middle - 1 : sample_head.next = sample_head.next.next
        
        return head
