package src.easy;

import java.util.LinkedList;
import java.util.Queue;

class ConvertSortedArrayToBST {
	public TreeNode sortedArrayToBST(int[] nums) {
		int len = nums.length, i = 1;
		TreeNode head;
		Queue<TreeNode> q = new LinkedList<>();
		if(len == 0)
			return null;
		head = new TreeNode(nums[0]);
		q.add(head);
		while (i < len) {
			int levelNum = q.size();
			for (int j = 0; j< levelNum && i < len; j++){
				TreeNode tempNode = q.poll();
				TreeNode left = new TreeNode(nums[i++]);
				tempNode.left = left;
				q.add(left);
				if ( i < len) {
					TreeNode right = new TreeNode(nums[i++]);
					tempNode.right = right;
					q.add(right);
				}
				
				
			}
		}
		
		return head;
	
	}
}