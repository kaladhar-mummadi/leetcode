package src.easy;

class LengthOfLastWord {
	public int lengthOfLastWord(String s) {
		int i = s.length() - 1;
		int max_len = 0, temp_len = 0;
		while (i >= 0) {
			if (s.charAt(i) != ' ') {
				temp_len += 1;
				
			}
			
			if (temp_len != 0 && s.charAt(i) == ' ') {
				break;
			}
			
			i -= 1;
		}
		max_len = temp_len;
		
		
		return max_len;
	}
}