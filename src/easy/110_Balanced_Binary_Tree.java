package src.easy;

class BalancedBinaryTree {
	public boolean isBalanced(TreeNode root) {
		int height = getHeight(root);
		if ( height == -1) {
			return false;
		} else {
			return true;
		}
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
}