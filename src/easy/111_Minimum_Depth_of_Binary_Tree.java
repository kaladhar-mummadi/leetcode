package src.easy;

class MinimumDepthOfBinaryTree {
	public int minDepth(TreeNode root) {
		return getHeight(root);
	}
	
	public int getHeight(TreeNode root) {
		if (root == null){
			return 0;
		}
		
		int left = getHeight(root.left);
		int right = getHeight(root.right);

		if ( left == 0) {
			return right +1;
		} else if(right == 0 || left < right) {
			return left + 1;
		}  else {
			return right + 1;
		}
	}
}