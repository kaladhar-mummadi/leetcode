package src.easy;
import java.util.*;

class BinaryTreeLevelOrderTraversal2 {
	
	public List<List<Integer>> levelOrderBottom(TreeNode root) {
		Queue<TreeNode> q = new PriorityQueue<>();
		List<List<Integer>> allValues = new ArrayList<List<Integer>>();
		
		if ( root != null)
			q.add(root);
		while (!q.isEmpty()) {
			List<Integer> levelNumbers = new ArrayList<>();
			Queue<TreeNode> tempQueue = new LinkedList<>();
			while (!q.isEmpty()) {
				
				TreeNode temp = q.remove();
				levelNumbers.add(temp.val);
				
				if (temp.left != null) {
					tempQueue.add(temp.left);
				}
				if (temp.right != null) {
					tempQueue.add(temp.right);
				}
			}
			
			if (levelNumbers.size() != 0) {
				allValues.add(0,levelNumbers);
				
			}
			
			if (!tempQueue.isEmpty()) {
				q = tempQueue;
			}
			
		}
		return allValues;
	}
	
//	public void traverseLevel(TreeNode root, List<List<Integer>> values, Queue<TreeNode> q){
//		List<Integer> levelNumbers = new ArrayList<>();
//		TreeNode temp = root;
//		while(temp != null ){
//			q.add(temp.left);
//			q.add(temp.right);
//
//
//			levelNumbers.add(temp.val);
//
//			temp = q.remove();
//
//		}
//		q.add(null);
//
//		traverseLevel(q.remove(), values, q);
//	}
}