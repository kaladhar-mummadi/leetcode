package src.easy;

class ExcelSheetColumnNumber {
	public int titleToNumber(String s) {
		int i = 0;
		int res = 0;
		
		while (i<s.length()) {
			int temp = s.charAt(i) - 64;
			res = 26*res + temp;
			i++;
		}
	return res;
	}
}