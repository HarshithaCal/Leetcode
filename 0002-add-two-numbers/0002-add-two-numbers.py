# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        ans = []
        carry = 0
        while p1 and p2:
            sm = p1.val + p2.val + carry
            if sm >= 10:
                carry = 1
                sm = sm - 10
            else:
                carry= 0

            ans.append(sm)
            p1 = p1.next
            p2 = p2.next
        
        while p1:
            sm = p1.val+carry
            if sm >= 10:
                carry = 1
                sm -= 10
            else:
                carry = 0

            ans.append(sm)
            p1 = p1.next
        
        while p2:
            sm = p2.val+carry
            if sm >= 10:
                carry = 1
                sm -= 10
            else:
                carry = 0


            ans.append(sm)
            p2 = p2.next
        if carry:
            ans.append(carry)
        print(ans)
        # return ans


        # Convert result list to a linked list
        dummy_head = ListNode(0)
        current = dummy_head
        for val in ans:
            current.next = ListNode(val)
            current = current.next

        return dummy_head.next

        