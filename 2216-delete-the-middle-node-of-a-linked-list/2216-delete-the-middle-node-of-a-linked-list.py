# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #optimized approach using fast and slow 
        if head == None:
            return None
        prev = ListNode() #prev to the curr node so dummy node before head
        prev.next = head
        slow = prev
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        return prev.next



        # #find the mid node number
        # length = 0
        # p = head
        # if head:
        #     length += 1
        #     p = p.next
        # while p:
        #     length += 1
        #     p = p.next
        
        # mid = floor(length/2)
        # print("mid index  value is ", mid)

        # #Corner case where there is only 1 element
        # if mid == 0:
        #     head = None
        #     return head


        # count = 1
        # p1 = head

        # # get p1 such that p1.next is the mid index
        # while count< mid:
        #     p1 = p1.next
        #     count += 1
        
        # q = p1.next
        # p1.next = q.next
        # return head








        