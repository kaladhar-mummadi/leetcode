package src.easy;

class IntersectionOfTwoLinkedLists {
	public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
		// seen the solution
		ListNode pA = headA, pB = headB;
		int i = 0;
		if (pA == null || pB == null) {
			return null;
		}
		
		while (pA != pB) {
			if (i > 2) {
				return null;
			}
			pA = pA.next;
			pB = pB.next;
			if (pA == null) {
				pA = headB;
				i += 1;
			}
			if (pB == null) {
				pB = headA;
				i += 1;
			}
		}
		
		return pA;
		
	}
}