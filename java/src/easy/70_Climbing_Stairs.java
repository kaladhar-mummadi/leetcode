package src.easy;

class ClimbingStairs {
	
	// BruteForce
	public int climb_stairs(int i, int steps) {
		if (i > steps) {
			return 0;
		}
		if (i == steps){
			return 1;
		}
		
		return climb_stairs(i+1,steps) + climb_stairs(i+2, steps);
	}
	public int climbStairs_bruteForce(int n) {
		int[] memo = new int[n+1];
		return climb_stairs(0,n);
	}
	
	
	// BruteForce with memoization
	public int climb_stairs(int i, int steps, int[] memo) {
		if (i > steps) {
			return 0;
		}
		if (i == steps){
			return 1;
		}
		if(memo[i] > 0) {
			return memo[i];
		}
		
		memo[i] = climb_stairs(i+1,steps, memo) + climb_stairs(i+2, steps, memo);
		
		return memo[i];
	}
	public int climbStairs_bruteForce_withmemo(int n) {
		int[] memo = new int[n+1];
		return climb_stairs(0,n, memo);
	}
	
	
	//dynamic programming which is equivalent to finding nth fibonacci number
	
	
	//fibonacchi forumla
	public int climbStairs(int n) {
		double sqrt5=Math.sqrt(5);
		double fibn=Math.pow((1+sqrt5)/2,n+1)-Math.pow((1-sqrt5)/2,n+1);
		return (int)(fibn/sqrt5);
	}
	
	
}