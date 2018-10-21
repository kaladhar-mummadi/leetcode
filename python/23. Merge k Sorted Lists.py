from  linked_list_utils import get_ll_from_array
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        head = res

        while l1 and l2:
            if l1.val < l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        if l1:
            res.next = l1

        if l2:
            res.next = l2
        head = head.next
        return head
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        i = 0
        head = None
        while i < len(lists):
            head = self.mergeTwoLists(head, lists[i])
            i += 1
        return head

sol = Solution()
sol.mergeKLists([get_ll_from_array([1,4,5]),get_ll_from_array([1,3,4]), get_ll_from_array([2,6])])