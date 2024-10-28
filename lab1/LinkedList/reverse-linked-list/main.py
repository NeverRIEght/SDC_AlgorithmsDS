from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        current_element = head
        previous_element = None
        next_element = None
        while current_element is not None:
            next_element = current_element.next
            current_element.next = previous_element
            previous_element = current_element
            current_element = next_element

        head = previous_element

        return head
