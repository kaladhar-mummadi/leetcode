class Solution {
    public int strStr(String haystack, String needle) {
        int haystack_len = haystack.length();
        int needle_len = needle.length();
        int i;
        if (haystack_len ==0 && needle_len == 0) {
        	return 0;
        }

        for(i=0; i< haystack_len; i++) {
        	int temp_i = i,j;
            int len = 0;
        	for(j=0; j < needle_len && temp_i < haystack_len; j++) {
        		if (haystack.charAt(temp_i) == needle.charAt(j)) {
                    len += 1;


        		}
        		temp_i += 1;
        	}

        	if (len == needle_len){
        		return i;
        	} 
        }

        return -1;
    }
}