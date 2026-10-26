/*
 * Problem: Valid Anagram
 * Platform: LeetCode
 * Link: https://leetcode.com/problems/valid-anagram/
 * Difficulty: Easy
 * Approach: Count each character in the first string, then subtract counts while scanning the second string.
 * Time Complexity: O(n)
 * Space Complexity: O(1) for the fixed English lowercase alphabet
 */
public class ValidAnagram {

    public static boolean isAnagram(String first, String second) {
        if (first.length() != second.length()) {
            return false;
        }

        int[] frequency = new int[26];
        for (int i = 0; i < first.length(); i++) {
            frequency[first.charAt(i) - 'a']++;
            frequency[second.charAt(i) - 'a']--;
        }

        for (int count : frequency) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isAnagram("anagram", "nagaram"));
        System.out.println(isAnagram("rat", "car"));
        System.out.println(isAnagram("", ""));
    }
}

