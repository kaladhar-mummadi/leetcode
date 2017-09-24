class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0, j = 0;
        int len = nums.length;
        int result = 0;
        while (j < len) {
        	if ( nums[i] != nums[j]){
        		result += 1;
                i += 1;
        		nums[i] = nums[j];
        		
        	}

        	j++;

        }

        if (j != 0){
        	result += 1;
        }

        return result;
    }
}