/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode resultHead = new ListNode(0);
        ListNode p = resultHead;

        while(true) {
        	ListNode temp;
        	if (l1 == null) {
                p.next = l2;
                
        		break;
        	} else if(l2 == null) {
        		p.next = l1;
        		break;
        	} 

        	if (l1.val <= l2.val) {
        		p.next = l1;
        		l1 = l1.next;
        		
        	} else {
        		p.next = l2;
        		l2 = l2.next;
        		
        	}


        	
        	p = p.next;
        }

        return resultHead.next;
    }
}