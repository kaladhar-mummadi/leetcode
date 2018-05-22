package src.easy;

class SingleNumber {
	public int singleNumber(int[] nums) {
		
		for(int i=1;i < nums.length; i++) {
			nums[i] = nums[i-1] ^ nums[i];
		}
		
		return nums[nums.length-1];
	
	}
}