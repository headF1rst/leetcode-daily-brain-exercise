# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from collections import defaultdict

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = defaultdict()

        while head:
            if head in dic:
                return True
            else:
                dic[head] = True
            head = head.next
        
        return False