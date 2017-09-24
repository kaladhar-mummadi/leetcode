package src.easy;

class ReverseInteger {
	public int reverse(int x) {
		long result = 0;
		boolean isNegative = false;
		if (x < 0) {
			int neg = -1;
			isNegative = true;
			x = neg * x;
			
			
		}
		
		while (x > 0) {
			
			int temp = x % 10;
			System.out.println(temp);
			x = x / 10;
			result = result * 10 + temp;
		}
		if (result > Integer.MAX_VALUE) {
			result = 0;
		}
		if (isNegative) {
			result = -1 * result;
		}
		return (int) result;
	}
}