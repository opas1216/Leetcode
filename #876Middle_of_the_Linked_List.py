# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            copy_listnode = head
            index = 0
            while head:
                index += 1
                head = head.next
            # print(f"Total amount of listnode = {index}\n")
            for count in range(int(index / 2)):
                copy_listnode = copy_listnode.next
            return copy_listnode






