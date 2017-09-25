package src.easy;

class AddBinary {
	public String addBinary(String a, String b) {
		int a_len = a.length();
		int b_len = b.length();
		int i=a_len-1, j = b_len-1;
		String res = "";
		int car = 0;
		while (true) {
			int sum = 0;
			if (i<0 && j<0) {
				break;
			}
			
			if (i>=0) {
				sum += (int) a.charAt(i) - '0';
			}
			if (j>=0) {
				sum += (int) b.charAt(j) - '0';
			}
			
			
			sum += car;
			
			if (sum == 2 ) {
				sum = 0;
				car = 1;
			} else if (sum == 3) {
				sum = 1;
				car = 1;
			} else{
				car = 0;
			}
			res = Integer.toString(sum) + res;
			
			i -=1;
			j -=1;
		}
		if (car == 1){
			res = Integer.toString(car)+res;
		}
		
		return res;
	}
}