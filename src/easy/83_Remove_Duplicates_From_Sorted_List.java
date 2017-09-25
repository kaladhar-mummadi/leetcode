
package src.easy;
//  Definition for singly-linked list.

class Solution {
	public ListNode deleteDuplicates(ListNode head) {
		ListNode p1 = head, p2 = head;
		
		while (p2 != null) {
			if (p1.val != p2.val) {
				p1.next = p2;
				p1 = p2;
			}
			
			p2 = p2.next;
			
		}
		
		if (p1 != null && p1.next != null && p1.val == p1.next.val) {
			p1.next = null;
		}
		return head;
		
	}
	
	//Without extra pointer and extra condition at the end
//	ListNode current = head;
//    while (current != null && current.next != null) {
//		if (current.next.val == current.val) {
//			current.next = current.next.next;
//		} else {
//			current = current.next;
//		}
//	}
//    return head;
}