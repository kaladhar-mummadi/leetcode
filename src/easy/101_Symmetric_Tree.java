package src.easy;


class Symmetric_Tree {
	public boolean isSymmetric(TreeNode root) {
		if (root == null) {
			return true;
		}
		
		return checkSymmetry(root.left, root.right);
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