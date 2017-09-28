package src.easy;
import java.util.*;

class PascalsTriangle2 {
	public List<Integer> getRow(int rowIndex) {
		List<Integer> particularRowValues = new ArrayList<>();
		int i = rowIndex;
		long number = 1;
			for(int j = 0; j<= i; j++) {
				particularRowValues.add((int) number);
				number = number * (i - j) / (j + 1);
			}

		
		return particularRowValues;
		
	}
}