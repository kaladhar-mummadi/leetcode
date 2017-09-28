package src.easy;
import java.util.*;

class PascalsTriangle {
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> pascal = new ArrayList<List<Integer>>();
		
		for(int i=0; i < numRows; i++) {
			
			List<Integer> subarray = new ArrayList<>();
			
			for(int j = 0; j<i+1; j++) {
				if (j ==0 || i == j){
					subarray.add(1);
				} else {
					subarray.add(pascal.get(i - 1).get(j - 1) + pascal.get(i - 1).get(j));
				}
			
			}
			pascal.add(subarray);
		}
		
		return pascal;
		
	}
}