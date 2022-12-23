# 206. Reverse Linked List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        else:
            current = ListNode()

            while head:
                current.val = head.val
                # print(f"current = {current}\n")
                head = head.next
                if head is not None:
                    current.next = ListNode(current.val, current.next)
                # print(f"head = {head}\n")
                # print(f"current = {current}\n")
            return current
        # Better way from Leetcode
        # prev = None
        # while head:
        #     curr = head
        #     head = head.next
        #     curr.next = prev
        #     prev = curr
        # return prev
