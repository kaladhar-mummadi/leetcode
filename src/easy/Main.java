package src.easy;

import java.io.*;


class Main {
	public static void main(String[] args) {
		PlusOne istr = new PlusOne();
		int[] inp = {1,9};
		int[] inde = istr.plusOne(inp);
		System.out.print(inde);
	}
}