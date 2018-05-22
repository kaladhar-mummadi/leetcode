package src.easy;

class PalindromeNumber {
	    public long reverse(long x) {
        long result=0;
        boolean isNegative = false;
        if (x < 0) {
        	isNegative = true;
        	x = -1 * x;
        }
        while (x > 0){
        	long temp = x%10;
        	x = x/10;
        	result = result*10 + temp;
        }

        if (isNegative) {
        	result = -1*result;
        }
        return result;
    }

    public boolean isPalindrome(int x) {
        if (x < 0) {
    		return false;
    	}
        long reverse_num = reverse((long) x);
        if (x == reverse_num) {
        	return true;
        }

        return false;
    }
}