class Solution {
    public int maxSubArray(int[] nums) {
    	if (nums.length == 0){
    		return 0;
    	}
    	int max_val = Integet.MIN_VALUE;
    	int sum = 0;
    	for(int i=1;i < nums.length;i++){
    		if (sum <0){
    			sum = nums[i];
    		} else {
    			sum += A[i];
    		}

    		if (max < sum) {
    			max = sum;
    		}
    	}

    	return max;
        
    }
}