class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def get_ll_from_array(nums):
    if len(nums) == 0:
        return  None

    head = ListNode(nums[0])
    temp = head
    i = 1
    while i < len(nums):
        temp.next = ListNode(nums[i])
        temp = temp.next
        i += 1
    return head