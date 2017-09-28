package src.easy;

class ValidPalindrome {
	
	//TODO: implmenet is characteror digit function, and upper case to lower case for better understanding
	public boolean isPalindrome(String s) {
		int len = s.length();
		int i = 0, j = len -1;
		while (i < j){
			char a = (s.charAt(i) >= 65 && s.charAt(i) <= 90)? (char) (s.charAt(i) + 32) : s.charAt(i);
			char b = (s.charAt(j) >= 65 && s.charAt(j) <= 90)? (char) (s.charAt(j) + 32) : s.charAt(j);
			if (a == b){
				i += 1;
				j-= 1;
			} else if(!((a >= 97 && a<= 122) || (a >= 48 && a <= 57))) {
				i += 1;
			} else if(!((b >= 97 && b<= 122) || (b >= 48 && b <= 57))){
				j -= 1;
			} else{
				return false;
			}
		}
		
		return true;
	}
}