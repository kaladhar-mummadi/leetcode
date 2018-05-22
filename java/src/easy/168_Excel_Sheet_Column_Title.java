package src.easy;

class ExcelSheetColumnTitle {
	public String convertToTitle(int n) {
		String res = "";
		while(n > 0) {
			int temp = n % 26;
			if (temp == 0){
				temp = 26;
				n = n-1;
			}
			res = (char)('@'+ temp) + res;
			
			
			n = n / 26;
		}
		return res;
	}
}