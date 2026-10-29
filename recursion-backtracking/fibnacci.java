/*
 * Problem: fibnacci
 * Platform: leetcode
 * 
 * Difficulty: Easy
 * Approach: Use recursion to calculate the nth Fibonacci number.
 * Time Complexity: O(n)
 * Space Complexity: O(1)
 */
class Solution {
    public int fib(int n) {
        if( n==0)
            return   0 ;
        if( n==1)
            return 1 ;

        return fib(n-1)+ fib(n-2) ;

    }
}