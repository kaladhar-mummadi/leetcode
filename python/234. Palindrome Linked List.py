# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverserList_rec(self, prev, current, head):
        if current == None:
            return prev
        if current.next == None:
            current.next = prev
            prev.next = None
            head = current
            return current
        head = self.reverserList_rec(current, current.next, head)
        current.next = prev
        return head

    def findMiddle(self, head):
        turtle = head
        rabbit = head.next
        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
        return turtle.next

    def isPalindrome(self, head):
        if not head:
            return True
        mid = self.findMiddle(head)
        if mid:
            head_rev = self.reverserList_rec(mid, mid.next, mid)
        else:
            head_rev = mid
        while head != mid and head_rev != None:
            print(head.val, head_rev.val)
            if head.val != head_rev.val:
                return False
            head = head.next
            head_rev = head_rev.next
        return True