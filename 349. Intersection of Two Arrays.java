package binarySearch;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Solution {
	/**
	 * @param nums1 [1, 2, 2, 1]
	 * @param nums2 [2, 2]
	 * @return
	 */
	public int[] intersection(int[] nums1, int[] nums2) {
		Set<Integer> set = new HashSet<>();
		Arrays.sort(nums1);
		Arrays.sort(nums2);
		int i = 0;
		int j = 0;
		while(i < nums1.length && j < nums2.length) {
			if(nums1[i] < nums2[j])
				i++;
			else if(nums1[i] > nums2[j])
				j++;
			else {
				set.add(nums1[i]);
				i++;
				j++;
			}
		}
		int[] result = new int[set.size()];
		int k = 0;
		for(Integer num : set) {
			result[k++] = num;
		}
		return result;
		
	}

	public static void main(String[] args) {
		int[] nums1 = {1,2,2,1};
		int[] nums2 = {2,2};
		new Solution().intersection(nums1,nums2);
		int[] result = new Solution().intersection(nums1,nums2);
		for(int num: result) {
			System.out.println(num + " ");
		}
	}

}
