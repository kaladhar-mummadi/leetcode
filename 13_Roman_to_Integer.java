class Solution {
    public int romanToInt(String s) {
        HashMap<Character,Integer> nums = new HashMap<Character, Integer>();
        nums.put('I',1);
        nums.put('V',5);
        nums.put('X',10);
        nums.put('L',50);
        nums.put('C',100);
        nums.put('D',500);
        nums.put('M',1000);

        int result = 0;
        if (s.length() == 0) {
            return 0;
        }
        
        System.out.println(s.charAt(0));

        int curr = 0, prev = nums.get(s.charAt(0));

        for (int i=1; i < s.length(); i++) {
        	curr = nums.get(s.charAt(i));
        	

        	if (prev < curr) {
        			prev = -1 * prev;

        	}
        	result += prev;
        	prev = curr;

        }

        result += prev;

        return result;

    }
}