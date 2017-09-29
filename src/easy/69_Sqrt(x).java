package src.easy;

class Sqrt {
	public int mySqrt(int x) {
		// Binary Search
		int left = 1, right = x, ans = 0;
		while (left <= right) {
			int mid = left + (right - left)/2;
			if(mid <= x/mid) {
				left = mid + 1;
				ans = mid;
			} else{
				right = mid - 1;
			}
		}
		
		
		return ans;
		
	}
	
	//There is also newton method and bit manipulation method
}