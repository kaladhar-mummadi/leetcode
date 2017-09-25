package src.easy;

class Solution {
    public String longestCommonPrefix(String[] strs) {
    	int i = 0,j = 0;
    	int len = strs.length;
    	String res = "";
    	int[] lengths = new int[strs.length];
        if (strs.length == 0){
            return "";
        }
    	while (true) {

    		char first_char = '\0';
            
    		for(j=0; j< strs.length; j++) {
    			if (i == 0 ){
                	lengths[j] = strs[j].length();
            	}

                if ( i < lengths[j]) {
                    first_char = strs[0].charAt(i);
                } else {
                    break;
                }
    			if (strs[j].charAt(i) != first_char) {
    				break;
    			}
    		}

    		i += 1;

             
    		if (len == j ){
    			res += first_char;
    		} else {
    			break;
    		}

    	}
    	return res;
    }
}