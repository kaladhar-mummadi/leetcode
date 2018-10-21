# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        tail = head
        i = 0
        k = k-1
        first = head
        second = head.next
        third = head.next.next
        while third != None:
            if i < k:
                second.next = first
                first = second
                second = third
                third = third.next
                i += 1
            else:
                tail.next = third
                first = tail
                i = 0
