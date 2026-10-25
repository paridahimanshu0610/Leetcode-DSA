import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        temp = []
        count = 0

        for ll in lists:
            if ll:
                temp.append((ll.val, count, ll))
                count += 1
        heapq.heapify(temp)

        curr = dummy = ListNode()

        while len(temp)!=0:
            _, _, temp_node = heapq.heappop(temp)
            curr.next = temp_node
            curr = temp_node
            
            if temp_node.next: 
                heapq.heappush(temp, (temp_node.next.val, count, temp_node.next))
                count += 1
        
        return dummy.next