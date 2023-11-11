# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def iter_link(head):

            value = []
            sample_head = head

            while sample_head :

                value.append(sample_head.val)
                sample_head = sample_head.next

            return value 

        val_1 = iter_link(l1)
        val_2 = iter_link(l2)

        if len(val_1) > len(val_2) : val_2 += [0] * (len(val_1) - len(val_2))
        elif len(val_2) > len(val_1) : val_1 += [0] * (len(val_2) - len(val_1))

        val_1 += [0]
        val_2 += [0]

        carry = None
        added = []

        print(val_1 , val_2)

        for index in range(len(val_1)) : 

            value = val_1[index] + val_2[index]

            if carry : 
                value += int(carry)
                carry = None

            value = str(value) 

            if len(value) > 1 : 

                carry = value[:-1]

            added.append(value[-1])

        if added[-1] == '0' : added.pop(-1)

        dummy_head = ListNode(0)
        tail = dummy_head

        for val in added:

            new_node = ListNode(int(val))
            
            tail.next = new_node
            tail = tail.next

        result = dummy_head.next 
        dummy_head.next = None

        return result
