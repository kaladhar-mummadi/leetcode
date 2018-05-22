package src.easy;

class MaximumDepthOfBinaryTree {
	public int maxDepth(TreeNode root) {
		if(root == null){
			return 0;
		}
		
		int left = maxDepth(root.left);
		int right = maxDepth(root.right);
		if(left < right){
			return right + 1;
		}else {
			return left + 1;
		}
	}
}