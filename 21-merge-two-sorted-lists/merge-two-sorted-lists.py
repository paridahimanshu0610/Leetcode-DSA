# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list0: ListNode | None) -> ListNode | None:
        curr0, curr1 = list0, list1
        prev0 = None

        if curr0 is None:
            return curr1
        elif curr1 is None:
            return curr0
        
        if curr1.val <= curr0.val:
            temp = curr1.next
            curr1.next = curr0
            prev0 = curr1
            curr1 = temp
            list0 = prev0
        else:
            prev0, curr0 = curr0, curr0.next

        while curr0 != None and curr1 != None:
            if curr1.val <= curr0.val:
                temp = curr1.next
                curr1.next = curr0
                if prev0:
                    prev0.next = curr1
                prev0 = curr1
                curr1 = temp
            else:
                prev0, curr0 = curr0, curr0.next
        
        if curr1:
            if prev0:
                prev0.next = curr1
            else:
                list0 = curr1

        return list0