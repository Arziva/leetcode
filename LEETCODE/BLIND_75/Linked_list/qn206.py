# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head): 
        prev = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = prev #changing direction of next
            prev = curr
            curr = curr_next 
        return prev

        #have to try recursive
            

