package src.easy;

import java.util.*;


class TwoSum {
	public int[] twoSum(int[] nums, int target) {
		int num_len = nums.length;
		int[] result = new int[2];
		HashMap<Integer, Integer> outputs = new HashMap<Integer, Integer>();
		for (int i = 0; i < num_len; i++) {
			int subtract_value = target - nums[i];
			
			if (outputs.containsKey(nums[i])) {
				
				result[0] = outputs.get(nums[i]);
				result[1] = i;
				return result;
			} else {
				
				outputs.put(subtract_value, i);
			}
			
		}
		
		return result;
	}
}