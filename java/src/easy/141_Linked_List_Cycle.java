package src.easy;

 class LinkedListCycle {
	public boolean hasCycle(ListNode head) {
		ListNode oneStepper = head , twoStepper = null;
		if (head != null){
			twoStepper = head.next;
		}
		
		while (twoStepper != null) {
			if(oneStepper == twoStepper) {
				return true;
			}
			oneStepper = oneStepper.next;
			twoStepper = twoStepper.next;
			if (twoStepper == null) {
				return false;
			}
			twoStepper = twoStepper.next;
		}
		
		return false;
	
	}
}