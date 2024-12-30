# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
       # 1) Find the middle via slow & fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2) Reverse the second half in-place
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # Now 'prev' is the head of the reversed second half
        
        # 3) Traverse from both ends simultaneously
        # left starts at original head, right starts at 'prev'
        max_sum = 0
        left, right = head, prev
        while right:
            twin_sum = left.val + right.val
            max_sum = max(max_sum, twin_sum)
            left = left.next
            right = right.next
        
        return max_sum
        
        