package src.easy;

/**
 * Created by kaladhar on 26/09/17.
 */
public class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;
	
	TreeNode(int x) {
		val = x;
	}
	
	public int getHeight(TreeNode root) {
		if (root == null){
			return 0;
		}
		
		int left = getHeight(root.left) + 1;
		int right = getHeight(root.right) + 1;
		
		if(left == 0 || right == 0 || Math.abs(right - left) > 1){
			return -1;
		}
		if ( left < right) {
			return right;
		} else {
			return left;
		}
	}
	
	public boolean checkSymmetry(TreeNode p, TreeNode q) {
		if (p == null && q == null) {
			return true;
		}
		
		if (p == null || q == null) {
			return false;
		}
		if (p.val == q.val) {
			return checkSymmetry(p.left, q.right) && checkSymmetry(p.right, q.left);
		}
		
		return false;
		
	}
}

