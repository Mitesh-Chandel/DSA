/*
 * Problem: Two Sum
 * Platform: LeetCode
 * Link: https://leetcode.com/problems/two-sum/
 * Difficulty: Easy
 * Approach: Store each number's index in a hash map and check whether its complement has already appeared.
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> indexByValue = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (indexByValue.containsKey(complement)) {
                return new int[] {indexByValue.get(complement), i};
            }
            indexByValue.put(nums[i], i);
        }

        return new int[0];
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum(new int[] {2, 7, 11, 15}, 9)));
        System.out.println(Arrays.toString(twoSum(new int[] {3, 2, 4}, 6)));
        System.out.println(Arrays.toString(twoSum(new int[] {3, 3}, 6)));
    }
}

