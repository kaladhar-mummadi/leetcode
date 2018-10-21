class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res
        i = 0
        j = 0
        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        while l1:
            res.next = l1
            res = res.next
            l1 = l1.next
        while l2:
            res.next = l2
            res = res.next
            l2 = l2.next
        head = head.next
        return head
