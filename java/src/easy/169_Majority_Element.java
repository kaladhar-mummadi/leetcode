package src.easy;


import java.util.HashMap;

class MajorityElement {
//	public int majorityElement(int[] nums) {
//		HashMap<Integer, Integer> values = new HashMap();
//		int half_len = nums.length/2;
//		int res = 0;
//
//		for (int i=0; i < nums.length; i++) {
//			int temp = nums[i];
//			if(values.containsKey(temp)) {
//				values.put(temp,values.get(temp)+1) ;
//			} else{
//				values.put(temp,0) ;
//			}
//
//			if(values.get(temp) >= half_len) {
//				res = temp;
//				break;
//			}
//		}
//
//		return res;
//	}
	
	//Moore’s Voting Algorithm
	public int majorityElement(int[] nums) {
		int count = 0; int res = 0;
		for(int num: nums){
			if (count == 0) {
				count++;
				res = num;
			} else if(res == num) {
				count++;
			} else{
				count--;
			}
		}
		return res;
	}
}