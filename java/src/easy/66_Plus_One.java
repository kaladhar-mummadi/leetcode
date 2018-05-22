package src.easy;

class PlusOne {
	public int[] plusOne(int[] digits) {
		int i = digits.length-1;
		int car = 1;
		while (i>=0) {
			int temp_sum = digits[i]+car;
			car = temp_sum/10;
			if(car == 0){
				digits[i] = temp_sum;
				break;
			}else {
				digits[i] = 0;
			}
			i -= 1;
			
		}
		
		if (car != 0) {
			int[] newDigits = new int[digits.length+1];
			i = digits.length-1;
			while(i>=0) {
				newDigits[i+1] = digits[i];
				
				i -=1;
			}
			newDigits[i] = car;
			return newDigits;
		}
		
		return digits;
		
	}
}