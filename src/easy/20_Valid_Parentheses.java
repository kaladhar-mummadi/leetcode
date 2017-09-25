package src.easy;

import java.util.*;
class ValidParanthases {
	public boolean isValid(String s) {
		int str_len = s.length();
		HashMap<Character, Character> braces = new HashMap<Character, Character>();
		Stack<Character> st = new Stack<Character>();
		boolean result = false;
		braces.put('(', ')');
		braces.put('{', '}');
		braces.put('[', ']');
		
		if (str_len % 2 != 0) {
			return result;
		}
		int i = 0;
		
		for (i = 0; i < (str_len); i++) {
			if (braces.containsKey(s.charAt(i))) {
				st.push(s.charAt(i));
			} else {
				while (!st.empty()) {
					char openBrace = st.pop();
					if (braces.get(openBrace) != s.charAt(i)) {
						result = false;
						return result;
						
					} else {
						result = true;
					}
					
					i += 1;
					
				}
			}
		}
		return result;
	}
}