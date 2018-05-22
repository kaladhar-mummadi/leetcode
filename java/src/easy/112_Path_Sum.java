package src.easy;

class PathSum {
	public boolean hasPathSum(TreeNode root, int sum) {
		return checkIfHasPathSum(root, sum, 0);
	}
	
	public boolean checkIfHasPathSum(TreeNode root, int checksum, int toadd) {
		if (root == null) {
			return false;
		}
		root.val += toadd;
		if(root.val == checksum && root.left == null && root.right == null) {
			return true;
		}
		
		return checkIfHasPathSum(root.left, checksum, root.val) || checkIfHasPathSum(root.right, checksum, root.val);
	}
}