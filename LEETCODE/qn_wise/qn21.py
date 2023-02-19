# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if(l1.val<l2.val):
        l1.next = self.mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = self.meregeTwoLists(l1,l2.next)
        return l2
list1 = [1,2,4]
list2 = [1,3,4]
l = mergeTwoLists(list1 ,list2)
